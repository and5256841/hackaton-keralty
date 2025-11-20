"""
Configuration management for Digital Twin Health MVP
Handles environment variables and application settings
"""
import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # OpenAI Configuration
    openai_api_key: Optional[str] = None
    openai_model: str = "gpt-4-turbo-preview"

    # Database Configuration
    # SQLite para demo rápido (cambiar a PostgreSQL en producción)
    database_url: str = "sqlite:///./digital_twin.db"
    analytics_database_url: Optional[str] = None

    # Application Settings
    app_name: str = "Digital Twin Health MVP"
    app_version: str = "1.0.0"
    debug: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "allow"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # If analytics DB not specified, use main database
        if not self.analytics_database_url:
            self.analytics_database_url = self.database_url

    def validate_openai_config(self) -> bool:
        """Validate that OpenAI API key is configured"""
        if not self.openai_api_key:
            raise RuntimeError(
                "⚠️  OPENAI_API_KEY no está configurada.\n"
                "Por favor configura la variable de entorno OPENAI_API_KEY "
                "antes de usar funcionalidades de IA.\n"
                "Puedes copiar .env.example a .env y agregar tu API key."
            )
        return True


# Global settings instance
settings = Settings()
