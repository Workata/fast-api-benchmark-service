from assertpy import assert_that
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from ...crud import get_items


def make_url() -> str:
    return "/api/items"


def test_create_item(client: TestClient, db: Session) -> None:
    assert_that(len(get_items(db))).is_equal_to(0)
    response = client.post(make_url(), json={"title": "New item", "description": "Dummy desc"})
    assert_that(len(get_items(db))).is_equal_to(1)

    expected_content = {"id": 1, "title": "New item", "description": "Dummy desc"}
    assert_that(response.status_code).is_equal_to(201)
    assert_that(response.json()).is_equal_to(expected_content)

    new_item = get_items(db)[0]
    assert_that(new_item.title).is_equal_to("New item")
    assert_that(new_item.description).is_equal_to("Dummy desc")
