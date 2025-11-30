"""
Configuration for Visual Search Engine.
"""

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Visual search settings."""

    # Azure Computer Vision
    vision_endpoint: str = Field(..., env="AZURE_VISION_ENDPOINT")
    vision_key: str = Field(..., env="AZURE_VISION_KEY")

    # Azure AI Search
    search_endpoint: str = Field(..., env="AZURE_SEARCH_ENDPOINT")
    search_key: str = Field(..., env="AZURE_SEARCH_KEY")
    search_index: str = Field(default="visual-search-index", env="AZURE_SEARCH_INDEX")

    # Azure Blob Storage
    storage_connection_string: str = Field(..., env="AZURE_STORAGE_CONNECTION_STRING")
    storage_container: str = Field(default="images", env="AZURE_STORAGE_CONTAINER")

    class Config:
        env_file = ".env"


settings = Settings()
