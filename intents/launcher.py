import os, subprocess, shlex, sys
from pathlib import Path

ALIASES = {
    "spotify": "spotify",
    "vlc": "vlc",
    "notepad": "notepad" if os.name == "nt" else "nano",
}

def launch(target: str):
    target = target.lower().strip()
    cmd = ALIASES.get(target, target)
    try:
        if Path(cmd).exists():
            subprocess.Popen([cmd], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.Popen(shlex.split(cmd), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return f"J’ai lancé « {target} ». Si ça plante, c’était une surprise immersive."
    except Exception as e:
        return f"Impossible de lancer « {target} » : {e}"
