from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn


class Settings(BaseSettings):
    # Приложение
    app_name: str = "CargoTracker"
    app_debug: bool = False

    # DB
    db_url: PostgresDsn = (
        "postgresql+asyncpg:///postgres:password@localhost:5432/postgres"
    )
    db_echo: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()
