from typing import Any, List
from unittest import mock

from assertpy import assert_that
from fastapi.testclient import TestClient

from ...utils import JsonLoader


def make_url() -> str:
    return "/api/report"


@mock.patch.object(JsonLoader, "load")
def test_get_report(mock_load: mock.MagicMock, client: TestClient) -> None:
    report: List[Any] = []
    mock_load.return_value = report
    response = client.get(make_url())

    expected_reponse = {"users": report}
    assert_that(response.json()).is_equal_to(expected_reponse)
