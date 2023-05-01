from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_204_NO_CONTENT, HTTP_200_OK, HTTP_201_CREATED
from sqlalchemy.orm import Session
from .models import Item
from typing import List, Dict, Any

from . import crud, schemas
from .database import get_db
from .utils import JsonLoader


router = APIRouter(prefix="/api", tags=["items"])


@router.get("/items", response_model=list[schemas.Item], status_code=HTTP_200_OK)
def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[Item]:
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/items/{item_id}", response_model=schemas.Item, status_code=HTTP_200_OK)
def get_item(item_id: int, db: Session = Depends(get_db)) -> Item:
    item = crud.get_item(db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/items", response_model=schemas.Item, status_code=HTTP_201_CREATED)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)) -> Item:
    return crud.create_item(db=db, item=item)


@router.delete("/items/{item_id}", status_code=HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)) -> None:
    item = crud.delete_item(db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")


@router.patch("/items/{item_id}", response_model=schemas.Item, status_code=HTTP_200_OK)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)) -> Item:
    updated_item = crud.update_item(db, item_id=item_id, item_data=item)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item


@router.get("/report", status_code=HTTP_200_OK)
def read_report() -> Dict[Any, Any]:
    report = JsonLoader.load(file_path="./src/data/health_report.json")
    return {"users": report}
