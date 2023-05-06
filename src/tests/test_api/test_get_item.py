from typing import Optional
from assertpy import assert_that
from fastapi.testclient import TestClient


def make_url(item_id: Optional[int] = None) -> str:
    if item_id:
        return f"/api/items/{item_id}"
    return "/api/items"


def test_retrieve_item(client: TestClient) -> None:
    response = client.get(make_url())
    print(response.status_code)
    print(response.content)
    assert_that(response.status_code).is_equal_to(200)
