from typing import Dict

from fastapi import FastAPI

from . import api, models
from .database import engine

models.BaseModel.metadata.create_all(bind=engine)  # type: ignore

app = FastAPI()

app.include_router(api.router)


@app.get("/hello")
def read_root() -> Dict[str, str]:
    return {"Hello": "World"}
