from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/hello")
def read_root() -> Dict[str, str]:
    return {"Hello": "World"}


