from fastapi import FastAPI
from . import api
from .database import BaseModel, engine, settings


TEST_ENV = "test"

# ? workaround for pipeline - can be implemented better
if not settings.environment == TEST_ENV:
    BaseModel.metadata.create_all(bind=engine)  # type: ignore

app = FastAPI()
app.include_router(api.router)
