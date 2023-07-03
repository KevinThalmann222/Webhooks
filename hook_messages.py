"""Autor: Kevin Thalmann."""
import socket

HOSTNAME = socket.gethostname()

def get_message(text_01: str, text_02: str) -> None:
    """Return Text."""
    return f"""
    Hallo zusammen,

    der Tag {text_01} wurde released.

    Hier sind alle Änderungen:
    {text_02}

    Diese Nachricht wurde automatisch vom Rechner {HOSTNAME} versendet.

    """
