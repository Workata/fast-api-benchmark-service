from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class ItemUpdate:
    title: Optional[str]
    description: Optional[str]


class Item(ItemBase):
    class Config:
        orm_mode = True