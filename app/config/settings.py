from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # -------------------------
    # App
    # -------------------------
    app_name: str = Field(default="AI Assistant V3", alias="APP_NAME")
    app_env: str = Field(default="development", alias="APP_ENV")
    debug: bool = Field(default=True, alias="DEBUG")

    # -------------------------
    # API
    # -------------------------
    host: str = Field(default="127.0.0.1", alias="HOST")
    port: int = Field(default=8000, alias="PORT")

    # -------------------------
    # Ollama
    # -------------------------
    ollama_host: str = Field(alias="OLLAMA_HOST")
    ollama_model: str = Field(alias="OLLAMA_MODEL")

    # -------------------------
    # Embeddings
    # -------------------------
    embedding_model: str = Field(alias="EMBEDDING_MODEL")

    # -------------------------
    # Database
    # -------------------------
    sqlite_db: str = Field(alias="SQLITE_DB")
    chroma_db: str = Field(alias="CHROMA_DB")

    # -------------------------
    # Logging
    # -------------------------
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    # -------------------------
    # Speech
    # -------------------------
    stt_model: str = Field(alias="STT_MODEL")
    tts_voice: str = Field(alias="TTS_VOICE")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()