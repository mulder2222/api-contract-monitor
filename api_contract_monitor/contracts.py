import json
from pathlib import Path


def load_contract(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_batch_config(path: str) -> list[dict]:
    return json.loads(Path(path).read_text(encoding="utf-8"))
