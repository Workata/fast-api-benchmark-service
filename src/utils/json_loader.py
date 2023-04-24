import json
from typing import Dict, Any


class JsonLoader:
    @classmethod
    def load(cls, file_path: str) -> Dict[Any, Any]:
        with open(file_path) as file:
            return json.load(file)  # type: ignore
