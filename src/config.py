from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    environment: str

    db_engine: str
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str

    # * optional settings cause test db is not needed for deploy
    test_db_engine: Optional[str]
    test_db_user: Optional[str]
    test_db_password: Optional[str]
    test_db_host: Optional[str]
    test_db_port: Optional[str]
    test_db_name: Optional[str]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings() -> Settings:
    return Settings()  # type: ignore
