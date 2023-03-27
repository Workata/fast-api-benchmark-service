from sqlalchemy.orm import Session
from typing import List

from . import models, schemas


def create_item(db: Session, item: schemas.ItemCreate) -> models.Item:
    item = models.Item(**item.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[models.Item]:
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> models.Item:
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def delete_item(db: Session, item_id: int) -> models.Item:
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        return None
    db.delete(item)
    db.commit()
    return item


def update_item(db: Session, item_id: int, item_data: schemas.ItemUpdate) -> models.Item:
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        return None
    item_dict = item_data.dict(exclude_unset=True)
    for key, value in item_dict.items():
        setattr(item, key, value)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
