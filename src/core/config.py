from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Configuration settings for the Privilege Academy API."""
    code_length: int = Field(6, description="Length of the generated short code for URLs")

    db_url:str = Field("sqlite:////data/db.sqlite3", description="Database URL for the SQLite database")

    class Config:
        """Configuration for Pydantic settings."""

        env_file = ".env"


settings = Settings()
