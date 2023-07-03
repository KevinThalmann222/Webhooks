"""Autor: Kevin Thalmann."""
import json

import requests

WEBHOOK_URL = "https://iavgroup.webhook.office.com/webhookb2/fb3738e5-b395-4630-bbea-05b0622afad7@cd726fc8-636c-4794-8425-41f9d8b0d7d5/IncomingWebhook/cc372bf27c144afb8acd8b902e4142d9/d83833fd-7393-48ce-9b10-748ed5368b05"
MESSAGE = """
Hallo zusammen,
das ist eine automatisch generierte Nachricht von einem Python-Skript.

Liebe Grüße,
Kevin
"""

def send_teams_message(webhook_url: str, message: str) -> None:
    """Send the message to Teams.

    Args:
        webhook_url: Teams webhool url
        message: your message
    """
    payload = {
        "text": message
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Error: {response.text}")


if __name__ == "__main__":
    send_teams_message(WEBHOOK_URL, MESSAGE)

