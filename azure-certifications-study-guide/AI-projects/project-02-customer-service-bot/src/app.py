"""
Main application entry point for the Customer Service Bot.
"""

import asyncio
from aiohttp import web
from botbuilder.core import (
    BotFrameworkAdapter,
    BotFrameworkAdapterSettings,
    ConversationState,
    MemoryStorage,
    UserState,
)
from botbuilder.schema import Activity

from config import settings
from bot import CustomerServiceBot
from services.openai_service import OpenAIService
from services.cosmos_service import CosmosService


# Create adapter
adapter_settings = BotFrameworkAdapterSettings(
    app_id=settings.bot_app_id,
    app_password=settings.bot_app_password,
)
adapter = BotFrameworkAdapter(adapter_settings)


# Error handler
async def on_error(context, error):
    print(f"Bot error: {error}")
    await context.send_activity("Sorry, an error occurred. Please try again.")


adapter.on_turn_error = on_error

# Create state and services
storage = MemoryStorage()
conversation_state = ConversationState(storage)
user_state = UserState(storage)
openai_service = OpenAIService()
cosmos_service = CosmosService()

# Create bot
bot = CustomerServiceBot(
    conversation_state=conversation_state,
    user_state=user_state,
    openai_service=openai_service,
    cosmos_service=cosmos_service,
)


async def messages(req: web.Request) -> web.Response:
    """Handle incoming messages."""
    if "application/json" in req.headers.get("Content-Type", ""):
        body = await req.json()
    else:
        return web.Response(status=415)

    activity = Activity().deserialize(body)
    auth_header = req.headers.get("Authorization", "")

    response = await adapter.process_activity(activity, auth_header, bot.on_turn)
    if response:
        return web.json_response(data=response.body, status=response.status)
    return web.Response(status=201)


app = web.Application()
app.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    print(f"Starting bot on port {settings.port}")
    web.run_app(app, host="0.0.0.0", port=settings.port)
