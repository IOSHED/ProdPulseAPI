from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    server_adress: str = "0.0.0.0"
    server_port: int = 8000

    random_secret: str = Field(min_length=128)
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    postgres_conn: PostgresDsn
    postgres_password: str
    postgres_username: str
    postgres_host: str
    postgres_port: int
    postgres_database: str
