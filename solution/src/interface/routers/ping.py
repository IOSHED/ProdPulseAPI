from fastapi import APIRouter


router_ping = APIRouter(tags=["ping"])


@router_ping.get("/ping")
async def _ping() -> str:
    return "pong"
