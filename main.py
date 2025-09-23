
from fastapi import FastAPI
from routers.auth_router import auth_router
from routers.order_router import order_router
from fastapi_jwt_auth import AuthJWT
from databases.schemas import Settings

app = FastAPI()

@AuthJWT.load_config # type: ignore #
def get_config():
    return Settings()


app.include_router(auth_router)