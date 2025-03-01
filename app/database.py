import json
from pathlib import Path

DATABASE_FILE = Path(__file__).parent.parent / 'tasks.json'


def load_data():
    if DATABASE_FILE.exists():
        with open(DATABASE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_data(data):
    with open(DATABASE_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
