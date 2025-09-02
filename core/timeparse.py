from datetime import datetime, timedelta
import re

def parse_when(text: str):
    text = text.lower().strip()
    now = datetime.now()
    m = re.search(r'(\d{1,2})[:h](\d{2})', text)
    if "demain" in text:
        if m: return datetime(now.year, now.month, now.day, int(m.group(1)), int(m.group(2))) + timedelta(days=1)
    if m:
        hh, mm = int(m.group(1)), int(m.group(2))
        dt = datetime(now.year, now.month, now.day, hh, mm)
        return dt if dt > now else dt + timedelta(days=1)
    # fallback: +10 min
    return now + timedelta(minutes=10)
