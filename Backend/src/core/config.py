from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Приложение
    app_name: str = "CargoTracker"
    app_debug: bool = False

    # DB
    db_url: str = "sqlite+aiosqlite:///./test.sqlite3"
    db_echo: bool = False

    # JWT
    secret_key: str = "some_secret_key"
    algorithm: str = "HS256"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()
