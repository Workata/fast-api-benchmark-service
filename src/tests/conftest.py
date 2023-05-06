from typing import Any, Iterator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from ..database import BaseModel, get_db, settings
from ..main import app


TEST_DB_URI = (
    f"{settings.test_db_engine}://{settings.test_db_user}:"
    f"{settings.test_db_password}@{settings.test_db_host}/{settings.test_db_name}"
)

engine = create_engine(TEST_DB_URI)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session() -> Iterator[Session]:

    BaseModel.metadata.drop_all(bind=engine)  # type: ignore
    BaseModel.metadata.create_all(bind=engine)  # type: ignore

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session: Any) -> Iterator[TestClient]:
    def override_get_db() -> Iterator[Session]:
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
