from core.storage import load_notes, save_notes
from datetime import datetime

def create_note(content: str):
    notes = load_notes()
    notes.append({"id": len(notes)+1, "content": content.strip(), "ts": datetime.now().isoformat()})
    save_notes(notes)
    return f"Note ajoutée ({len(notes)} au total)."

def list_notes():
    notes = load_notes()
    if not notes: return "Aucune note pour l’instant."
    return "\n".join([f"- [{n['id']}] {n['content']}" for n in notes])

def search_notes(query: str):
    notes = load_notes()
    found = [n for n in notes if query.lower() in n["content"].lower()]
    if not found: return "Rien trouvé. Tes notes sont timides."
    return "\n".join([f"- [{n['id']}] {n['content']}" for n in found])
