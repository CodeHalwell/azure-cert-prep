"""
Main bot activity handler.
"""

from botbuilder.core import ActivityHandler, TurnContext, ConversationState, UserState
from botbuilder.schema import ChannelAccount
from services.openai_service import OpenAIService
from services.cosmos_service import CosmosService


class CustomerServiceBot(ActivityHandler):
    """Customer service bot with OpenAI integration."""

    def __init__(
        self,
        conversation_state: ConversationState,
        user_state: UserState,
        openai_service: OpenAIService,
        cosmos_service: CosmosService,
    ):
        self.conversation_state = conversation_state
        self.user_state = user_state
        self.openai_service = openai_service
        self.cosmos_service = cosmos_service
        
        # State accessors
        self.conversation_data = self.conversation_state.create_property("ConversationData")
        self.user_profile = self.user_state.create_property("UserProfile")

    async def on_members_added_activity(
        self, members_added: list[ChannelAccount], turn_context: TurnContext
    ):
        """Handle new members joining the conversation."""
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    "Hello! I'm your AI customer service assistant. How can I help you today?"
                )

    async def on_message_activity(self, turn_context: TurnContext):
        """Handle incoming messages."""
        user_message = turn_context.activity.text
        conversation_id = turn_context.activity.conversation.id
        user_id = turn_context.activity.from_property.id
        
        # Get conversation history
        history = await self.cosmos_service.get_conversation_history(conversation_id)
        
        # Generate AI response
        response = await self.openai_service.generate_response(
            user_message=user_message,
            conversation_history=history,
            user_context={"user_id": user_id}
        )
        
        # Save to conversation history
        await self.cosmos_service.save_message(
            conversation_id=conversation_id,
            user_id=user_id,
            user_message=user_message,
            bot_response=response
        )
        
        await turn_context.send_activity(response)

    async def on_turn(self, turn_context: TurnContext):
        """Handle turn and save state."""
        await super().on_turn(turn_context)
        await self.conversation_state.save_changes(turn_context)
        await self.user_state.save_changes(turn_context)
