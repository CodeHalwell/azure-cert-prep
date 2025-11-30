"""
Cosmos DB service for conversation persistence.
"""

from datetime import datetime
from azure.cosmos import CosmosClient, PartitionKey
from config import settings


class CosmosService:
    """Service for Cosmos DB operations."""

    def __init__(self):
        self.client = CosmosClient(settings.cosmos_endpoint, settings.cosmos_key)
        self.database = self.client.create_database_if_not_exists(settings.cosmos_database)
        self.container = self.database.create_container_if_not_exists(
            id="conversations",
            partition_key=PartitionKey(path="/conversation_id"),
        )

    async def get_conversation_history(self, conversation_id: str) -> list[dict]:
        """Get conversation history for a conversation."""
        query = "SELECT * FROM c WHERE c.conversation_id = @conversation_id ORDER BY c.timestamp"
        parameters = [{"name": "@conversation_id", "value": conversation_id}]
        
        items = list(
            self.container.query_items(
                query=query,
                parameters=parameters,
                enable_cross_partition_query=True,
            )
        )
        return items

    async def save_message(
        self,
        conversation_id: str,
        user_id: str,
        user_message: str,
        bot_response: str,
    ) -> None:
        """Save a message exchange to the database."""
        item = {
            "id": f"{conversation_id}-{datetime.utcnow().timestamp()}",
            "conversation_id": conversation_id,
            "user_id": user_id,
            "user_message": user_message,
            "bot_response": bot_response,
            "timestamp": datetime.utcnow().isoformat(),
        }
        self.container.create_item(body=item)
