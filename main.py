import os, threading, time
from datetime import datetime
from rich import print
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler

from nlu import classify
from intents.notes import create_note, list_notes, search_notes
from intents.reminders import create_reminder, list_reminders
from intents.launcher import launch
from core.tts import speak
from core.storage import load_reminders, save_reminders

load_dotenv()

def reminder_tick():
    # Vérifie les rappels chaque 15s
    now = datetime.now()
    reminders = load_reminders()
    remaining = []
    for r in reminders:
        when = datetime.fromisoformat(r["when"])
        if when <= now:
            msg = f"[ALERTE] {when.strftime('%H:%M')} — {r['text']}"
            print(f"[bold red]{msg}[/bold red]")
            speak(msg)
        else:
            remaining.append(r)
    save_reminders(remaining)

def handle(user_input: str):
    parsed = classify(user_input)
    intent = parsed["intent"]; args = parsed.get("args", {})
    humor = parsed.get("humor","")

    if intent == "note.create":
        out = create_note(args["content"])
    elif intent == "note.list":
        out = list_notes()
    elif intent == "note.search":
        out = search_notes(args["query"])
    elif intent == "reminder.create":
        out = create_reminder(args["text"])
    elif intent == "reminder.list":
        out = list_reminders()
    elif intent == "app.launch":
        out = launch(args["target"])
    else:
        out = "On discute ! Pose-moi une question ou donne une commande."
    reply = f"{out}\n[i]{humor}[/i]"
    print(reply); speak(reply)

def main():
    print("[bold]Jarvis Lite — prêt.[/bold] (tapote 'exit' pour quitter)")
    sched = BackgroundScheduler()
    sched.add_job(reminder_tick, 'interval', seconds=15)
    sched.start()

    try:
        while True:
            text = input("> ").strip()
            if text.lower() in ("exit", "quit"): break
            if not text: continue
            handle(text)
    finally:
        sched.shutdown()

if __name__ == "__main__":
    main()
