from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]


class Item(BaseModel):
    id: int
    title: str
    description: str | None = None

    class Config:
        orm_mode = True
