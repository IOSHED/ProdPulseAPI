from typing import Any
from fastapi import APIRouter, Depends


router_auth = APIRouter(prefix="/auth", tags=["auth"])


@router_auth.post(
    "/register",
    status_code=201,
    response_model=RegisterResponse,
    response_model_exclude_none=True,
)
async def _register(
    user_schema_create: RegisterRequest,
    user_service: UserService = Depends(UserService),
) -> Any:
    db_user = await user_service.add_user(user_schema_create)
    return RegisterResponse(profile=db_user)


# @router_auth.post("/sign-in")
# async def sign_in(
#     uow: UOWDep, sign_data: Annotated[SignInSchema, Body()]
# ) -> TokenSchema:
#     is_authenticated = await UsersService().authenticate_user(uow, sign_data)
#     if is_authenticated:
#         return await signJWT(is_authenticated)
#     raise BaseRouterException(reason="Invalid username or password", status_code=401)
