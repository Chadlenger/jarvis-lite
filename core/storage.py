import json, os
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"
DATA.mkdir(exist_ok=True)

def _load(path, default):
    if not path.exists(): return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default

def _save(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")

def load_notes():
    return _load(DATA / "notes.json", [])

def save_notes(notes):
    _save(DATA / "notes.json", notes)

def load_reminders():
    return _load(DATA / "reminders.json", [])

def save_reminders(reminders):
    _save(DATA / "reminders.json", reminders)
