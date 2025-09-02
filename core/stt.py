import speech_recognition as sr

def listen_once(timeout=5, phrase_time_limit=10):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    return r.recognize_google(audio, language="fr-FR")
