"""
Configuration for Content Moderation System.
"""

import os
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Content moderation settings."""

    # Azure Content Safety
    content_safety_endpoint: str = Field(..., env="AZURE_CONTENT_SAFETY_ENDPOINT")
    content_safety_key: str = Field(..., env="AZURE_CONTENT_SAFETY_KEY")

    # Cosmos DB
    cosmos_endpoint: str = Field(..., env="COSMOS_ENDPOINT")
    cosmos_key: str = Field(..., env="COSMOS_KEY")
    cosmos_database: str = Field(default="moderation", env="COSMOS_DATABASE")

    # Moderation thresholds (0-7 scale)
    threshold_safe: int = Field(default=1, env="THRESHOLD_SAFE")
    threshold_review: int = Field(default=4, env="THRESHOLD_REVIEW")
    threshold_block: int = Field(default=6, env="THRESHOLD_BLOCK")

    class Config:
        env_file = ".env"


settings = Settings()
