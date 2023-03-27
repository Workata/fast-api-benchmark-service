from typing import Dict

from fastapi import FastAPI

from . import models, api, models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api.router)


@app.get("/hello")
def read_root() -> Dict[str, str]:
    return {"Hello": "World"}
