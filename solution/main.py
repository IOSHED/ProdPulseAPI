from fastapi import FastAPI
from src.infra.database.tortoise import lifespan_tortoise
from src.interface.exception import exception_handlers
from src.interface.routers import routers


app = FastAPI(
    debug=False,
    lifespan=lifespan_tortoise,
    exception_handlers=exception_handlers,
    root_path="/api",
    docs_url="/docs",
    redoc_url="/redoc",
    version="0.2.0",
    title="PROD v2: Pulse Backend",
    description="""
    Приложение должно представлять из себя HTTP сервер, реализующий необходимое API. 
    В наследие от предыдущей команды вам достался инстанс PostgreSQL, 
    который необходимо использовать для хранения данных.
    """,
)
app.include_router(routers)
