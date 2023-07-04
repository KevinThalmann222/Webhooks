"""Autor: Kevin Thalmann."""
import socket

HOSTNAME = socket.gethostname()

def get_message(title: str, description: str) -> None:
    """Return Text."""
    return f"""
    Hallo zusammen,

    es wurde ein neuer Tag Relead.

    Title: {title}

    Beschreibung:

    {description}


    -----------------
    Diese Nachricht wurde automatisch

    vom Rechner '{HOSTNAME}' versendet.
    """
