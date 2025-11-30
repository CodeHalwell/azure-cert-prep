"""
Configuration for Sentiment Analysis project.
"""

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Sentiment analysis settings."""

    # Azure Language Service
    language_endpoint: str = Field(..., env="AZURE_LANGUAGE_ENDPOINT")
    language_key: str = Field(..., env="AZURE_LANGUAGE_KEY")

    # Cosmos DB
    cosmos_endpoint: str = Field(..., env="COSMOS_ENDPOINT")
    cosmos_key: str = Field(..., env="COSMOS_KEY")
    cosmos_database: str = Field(default="sentiment", env="COSMOS_DATABASE")

    class Config:
        env_file = ".env"


settings = Settings()
