from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import Item
from typing import List

from . import crud, schemas
from .database import get_db


router = APIRouter(prefix="/api", tags=["items"])


@router.get("/items", response_model=list[schemas.Item])
def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[Item]:
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/items/{item_id}", response_model=schemas.Item)
def get_item(item_id: int, db: Session = Depends(get_db)) -> Item:
    item = crud.get_item(db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/items", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)) -> Item:
    return crud.create_item(db=db, item=item)


@router.delete("/items/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(get_db)) -> Item:
    item = crud.delete_item(db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.patch("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)) -> Item:
    item = crud.update_item(db, item_id=item_id, item_data=item)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
