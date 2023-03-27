from typing import Dict


from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models #crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/api/hello")
def read_root() -> Dict[str, str]:
    return {"Hello": "World"}


