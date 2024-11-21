import json
from pathlib import Path

DATABASE_FILE = Path(__file__).parent.parent / "tasks.json"

def load_data():
    if DATABASE_FILE.exists():
        with open(DATABASE_FILE, "r") as f:
            return json.load(f)
    return []

