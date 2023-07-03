"""Autor: Kevin Thalmann."""
import json
import socket

import requests

HOSTNAME = socket.gethostname()
MESSAGE = f"""
Hallo zusammen,

das ist eine automatisch generierte Nachricht von einem Python-Skript.

Gesendet vom Rechner: "{HOSTNAME}"

Liebe Grüße,
Kevin
"""

webhook_dict = [
    {
    "TEAM_KANAL": "Test Kevin",
    "URL": "https://iavgroup.webhook.office.com/webhookb2/fb3738e5-b395-4630-bbea-05b0622afad7@cd726fc8-636c-4794-8425-41f9d8b0d7d5/IncomingWebhook/570671a998d14278952ee9b39f221d52/d83833fd-7393-48ce-9b10-748ed5368b05",
    }
]


def send_teams_message(webhook_urls: list[dict], message: str) -> None:
    """Send the message to Teams.

    Args:
        webhook_urls: List of Teams webhool url
        message: your message
    """
    payload = {
        "text": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    for webhook  in webhook_urls:
        response = requests.post(webhook['URL'], data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            print(f"Message sent '{webhook['TEAM_KANAL']}' successfully!")
        else:
            print(f"Failed to send message to {webhook['TEAM_KANAL']}. Error: {response.text}")


if __name__ == "__main__":
    send_teams_message(webhook_dict, MESSAGE)

