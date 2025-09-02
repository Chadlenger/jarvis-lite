import os
import pyttsx3

_engine = None

def speak(text: str):
    global _engine
    if os.getenv("JARVIS_VOICE_ENABLED", "false").lower() != "true":
        return
    if _engine is None:
        _engine = pyttsx3.init()
    _engine.say(text)
    _engine.runAndWait()
