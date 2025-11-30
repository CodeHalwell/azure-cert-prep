"""
Configuration for Translation Service.
"""

import os
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Translation service settings."""

    # Azure Translator
    translator_key: str = Field(..., env="AZURE_TRANSLATOR_KEY")
    translator_endpoint: str = Field(..., env="AZURE_TRANSLATOR_ENDPOINT")
    translator_region: str = Field(default="eastus", env="AZURE_TRANSLATOR_REGION")

    # Azure Speech
    speech_key: str = Field(..., env="AZURE_SPEECH_KEY")
    speech_region: str = Field(default="eastus", env="AZURE_SPEECH_REGION")

    class Config:
        env_file = ".env"


settings = Settings()
