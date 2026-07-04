from pathlib import Path
import json

# root = one folder above src
PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_match(match_id: int):
    file_path = (
        PROJECT_ROOT
        / "open-data"
        / "data"
        / "events"
        / f"{match_id}.json"
    )

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)