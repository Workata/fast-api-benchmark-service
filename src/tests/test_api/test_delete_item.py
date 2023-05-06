import pytest
from assertpy import assert_that
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from ...crud import create_item, get_items
from ...schemas import ItemCreate


def make_url(item_id: int) -> str:
    return f"/api/items/{item_id}"


@pytest.fixture(autouse=True)
def create_items(db: Session) -> None:
    create_item(db, ItemCreate(title="Item 1"))
    create_item(db, ItemCreate(title="Item 2", description="Some description"))
    create_item(db, ItemCreate(title="Item 3"))


def test_delete_item(client: TestClient, db: Session) -> None:
    assert_that(len(get_items(db))).is_equal_to(3)
    response = client.delete(make_url(2))
    assert_that(len(get_items(db))).is_equal_to(2)

    expected_content = b""
    assert_that(response.status_code).is_equal_to(204)
    assert_that(response.content).is_equal_to(expected_content)
