import os
from typing import Literal
from dotenv import load_dotenv
load_dotenv()

SYSTEM = """Tu es Jarvis, assistant concis, utile, un peu taquin mais respectueux.
Renvoie du JSON strict avec:
{ "intent": "...", "args": { ... }, "humor": "..." }
Intents: note.create|note.search|note.list|reminder.create|reminder.list|app.launch|chit_chat
Si ambigu: propose intent chit_chat. 'humor' = une phrase courte drôle liée à la requête."""

def classify(user_input: str):
    # Version sans appel API (heuristiques simples)
    t = user_input.lower()
    if any(k in t for k in ["note:", "ajoute une note", "nouvelle note"]):
        return {"intent":"note.create","args":{"content":user_input.split(":",1)[-1].strip()}, "humor":"Mémoire d’éléphant, c’est moi."}
    if any(k in t for k in ["cherche", "retrouve", "recherche", "trouve"]) and "note" in t:
        return {"intent":"note.search","args":{"query":user_input.replace("note","" ).strip()}, "humor":"Sherlock des post-its."}
    if "liste" in t and "note" in t:
        return {"intent":"note.list","args":{}, "humor":"Prépare tes yeux, ça défile."}
    if any(k in t for k in ["rappelle", "rappel", "alarme"]):
        return {"intent":"reminder.create","args":{"text":user_input}, "humor":"Je mets le réveil, promesse de scout."}
    if "mes rappels" in t or ("liste" in t and "rappel" in t):
        return {"intent":"reminder.list","args":{}, "humor":"Agenda d’acier."}
    if any(k in t for k in ["ouvre", "lance", "démarre"]):
        return {"intent":"app.launch","args":{"target":user_input.replace("ouvre","" ).replace("lance","" ).replace("démarre","" ).strip()}, "humor":"Vroum, c’est parti."}
    return {"intent":"chit_chat","args":{"text":user_input}, "humor":"Je réponds plus vite qu’un café serré."}

