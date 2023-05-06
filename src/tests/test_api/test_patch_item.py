import pytest
from assertpy import assert_that
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from ...crud import create_item, get_item
from ...schemas import ItemCreate


def make_url(item_id: int) -> str:
    return f"/api/items/{item_id}"


@pytest.fixture(autouse=True)
def create_items(db: Session) -> None:
    create_item(db, ItemCreate(title="Item 1"))
    create_item(db, ItemCreate(title="Item 2", description="Some description"))
    create_item(db, ItemCreate(title="Item 3"))


def test_patch_item(client: TestClient, db: Session) -> None:
    response = client.patch(make_url(3), json={"description": "Updated description"})
    expected_content = {"id": 3, "title": "Item 3", "description": "Updated description"}

    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).is_equal_to(expected_content)
    updated_item = get_item(db, 3)
    assert_that(updated_item.description).is_equal_to("Updated description")  # type: ignore
