from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings read from environment variables and the .env file."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    gemini_api_key: SecretStr
    gemini_model: str
    tmdb_read_access_token: SecretStr
    lastfm_api_key: SecretStr


@lru_cache
def get_settings() -> Settings:
    """Return the settings, created once and reused on later calls."""
    return Settings()
