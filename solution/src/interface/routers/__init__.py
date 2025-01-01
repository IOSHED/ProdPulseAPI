from .ping import router_ping
from .country import router_country

from fastapi import APIRouter


included_routers = (
    router_ping,
    router_country,
)


routers = APIRouter()
for router in included_routers:
    routers.include_router(router)
