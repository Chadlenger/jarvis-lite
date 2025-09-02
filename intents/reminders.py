from core.storage import load_reminders, save_reminders
from core.timeparse import parse_when
from datetime import datetime

def create_reminder(text: str):
    when = parse_when(text)
    reminders = load_reminders()
    reminders.append({"id": len(reminders)+1, "when": when.isoformat(), "text": text})
    save_reminders(reminders)
    return f"Rappel programmé pour {when.strftime('%d/%m %H:%M')}."

def list_reminders():
    reminders = load_reminders()
    if not reminders: return "Aucun rappel. On vit dangereusement."
    def fmt(r):
        dt = datetime.fromisoformat(r["when"])
        return f"- [{r['id']}] {dt.strftime('%d/%m %H:%M')} — {r['text']}"
    return "\n".join(map(fmt, reminders))
