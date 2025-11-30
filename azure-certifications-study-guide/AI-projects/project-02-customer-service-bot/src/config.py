"""
Customer Service Bot configuration.
"""

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Bot application settings."""

    # Bot Configuration
    bot_app_id: str = Field(..., env="BOT_APP_ID")
    bot_app_password: str = Field(..., env="BOT_APP_PASSWORD")
    
    # Azure OpenAI
    openai_endpoint: str = Field(..., env="AZURE_OPENAI_ENDPOINT")
    openai_api_key: str = Field(..., env="AZURE_OPENAI_API_KEY")
    openai_deployment: str = Field(default="gpt-4o", env="AZURE_OPENAI_DEPLOYMENT")
    
    # Cosmos DB
    cosmos_endpoint: str = Field(..., env="COSMOS_ENDPOINT")
    cosmos_key: str = Field(..., env="COSMOS_KEY")
    cosmos_database: str = Field(default="botdb", env="COSMOS_DATABASE")
    
    # Application
    port: int = Field(default=3978, env="PORT")
    log_level: str = Field(default="INFO", env="LOG_LEVEL")

    class Config:
        env_file = ".env"


settings = Settings()
