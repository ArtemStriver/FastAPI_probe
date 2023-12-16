from fastapi import FastAPI

from src.auth.base_config import fastapi_users, auth_backend
from src.auth.schemas import UserRead, UserCreate

app = FastAPI(
    title="Trading App"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)
