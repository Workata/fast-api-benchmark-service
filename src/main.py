from fastapi import FastAPI
from . import api
from .database import BaseModel, engine, settings


TEST_ENV = "test"


if not settings.environment == TEST_ENV:
    BaseModel.metadata.create_all(bind=engine)  # type: ignore

app = FastAPI()
app.include_router(api.router)
