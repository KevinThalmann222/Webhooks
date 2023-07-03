"""Autor: Kevin Thalmann."""
import socket

HOSTNAME = socket.gethostname()

MESSAGE_PUSH = f"""
Hallo zusammen,

Es wurde etwas neues in den "master" gepusht.

Gesendet vom Rechner: "{HOSTNAME}"

Liebe Grüße,
Kevin
"""

MESSAGE_RELEASE = f"""
Hallo zusammen,

ein neues Release wurde erstellt.

Gesendet vom Rechner: "{HOSTNAME}"

Liebe Grüße,
Kevin
"""

MESSAGE_TEST = f"""
Hallo zusammen,

das ist eine automatisch generierte Nachricht von einem Python-Skript.

Gesendet vom Rechner: "{HOSTNAME}"

Liebe Grüße,
Kevin
"""
