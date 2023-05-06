from typing import Optional

import pytest
from assertpy import assert_that
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from ...crud import create_item
from ...schemas import ItemCreate


def make_url(item_id: Optional[int] = None) -> str:
    if item_id:
        return f"/api/items/{item_id}"
    return "/api/items"


@pytest.fixture(autouse=True)
def create_items(db: Session) -> None:
    create_item(db, ItemCreate(title="Item 1"))
    create_item(db, ItemCreate(title="Item 2", description="Some description"))
    create_item(db, ItemCreate(title="Item 3"))


def test_list_items(client: TestClient) -> None:
    response = client.get(make_url())
    expected_content = [
        {"id": 1, "title": "Item 1", "description": None},
        {"id": 2, "title": "Item 2", "description": "Some description"},
        {"id": 3, "title": "Item 3", "description": None},
    ]
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).is_equal_to(expected_content)


def test_retrieve_item(client: TestClient) -> None:
    response = client.get(make_url(2))
    expected_content = {"id": 2, "title": "Item 2", "description": "Some description"}
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).is_equal_to(expected_content)
