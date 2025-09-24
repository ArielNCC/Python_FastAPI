from fastapi import FastAPI
from routes.user import user

app = FastAPI(
        title="FastAPI MySQL-RESTAPI",
        description="first model of api",
        version="0.0.1",
        openapi_tags=[{
                "name": "users",
                "description": "users routes"

        }]
)

app.include_router(user)