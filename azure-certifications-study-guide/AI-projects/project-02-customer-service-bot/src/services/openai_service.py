"""
Azure OpenAI service for generating responses.
"""

from openai import AzureOpenAI
from config import settings


class OpenAIService:
    """Service for Azure OpenAI operations."""

    def __init__(self):
        self.client = AzureOpenAI(
            azure_endpoint=settings.openai_endpoint,
            api_key=settings.openai_api_key,
            api_version="2024-02-15-preview",
        )
        self.deployment = settings.openai_deployment
        
        self.system_prompt = """You are a helpful customer service assistant.
Your role is to:
- Answer customer questions politely and professionally
- Help resolve issues and provide solutions
- Escalate complex issues when needed
- Maintain a friendly, empathetic tone

If you don't know the answer, be honest and offer to connect them with a human agent."""

    async def generate_response(
        self,
        user_message: str,
        conversation_history: list[dict],
        user_context: dict,
    ) -> str:
        """Generate an AI response based on the conversation."""
        
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Add conversation history
        for msg in conversation_history[-10:]:  # Last 10 messages
            messages.append({"role": "user", "content": msg.get("user_message", "")})
            messages.append({"role": "assistant", "content": msg.get("bot_response", "")})
        
        # Add current message
        messages.append({"role": "user", "content": user_message})
        
        response = self.client.chat.completions.create(
            model=self.deployment,
            messages=messages,
            temperature=0.7,
            max_tokens=500,
        )
        
        return response.choices[0].message.content
