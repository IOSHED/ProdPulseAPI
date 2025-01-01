from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from tortoise.contrib.fastapi import RegisterTortoise

from src.infra.config import SETTINGS

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": SETTINGS.postgres_host,
                "port": SETTINGS.postgres_port,
                "user": SETTINGS.postgres_username,
                "password": SETTINGS.postgres_password,
                "database": SETTINGS.postgres_database,
            },
        },
    },
    "apps": {
        "server": {
            "models": [
                "aerich.models",
                "src.infra.database.models",
            ],
        }
    },
}


@asynccontextmanager
async def lifespan_tortoise(app: FastAPI) -> AsyncGenerator[None, None]:
    try:
        async with RegisterTortoise(
            app=app,
            config=TORTOISE_ORM,
            generate_schemas=True,
            add_exception_handlers=True,
        ):
            yield
    except Exception as _:
        raise
