"""
Configuration management for Document Processing project.
Loads environment variables and provides type-safe settings.
"""

import os
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Azure Document Intelligence
    document_intelligence_endpoint: str = Field(
        ..., env="AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT"
    )
    document_intelligence_key: str = Field(
        ..., env="AZURE_DOCUMENT_INTELLIGENCE_KEY"
    )

    # Azure OpenAI
    openai_endpoint: str = Field(..., env="AZURE_OPENAI_ENDPOINT")
    openai_api_key: str = Field(..., env="AZURE_OPENAI_API_KEY")
    openai_deployment_name: str = Field(
        default="gpt-4o", env="AZURE_OPENAI_DEPLOYMENT_NAME"
    )
    openai_api_version: str = Field(
        default="2024-02-15-preview", env="AZURE_OPENAI_API_VERSION"
    )

    # Azure Blob Storage
    storage_connection_string: str = Field(
        ..., env="AZURE_STORAGE_CONNECTION_STRING"
    )
    storage_container_name: str = Field(
        default="documents", env="AZURE_STORAGE_CONTAINER_NAME"
    )

    # Azure Key Vault (optional)
    key_vault_url: str | None = Field(default=None, env="AZURE_KEY_VAULT_URL")

    # Application settings
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    max_document_size_mb: int = Field(default=50, env="MAX_DOCUMENT_SIZE_MB")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Global settings instance
settings = Settings()
