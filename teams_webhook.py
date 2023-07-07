"""Autor: Kevin Thalmann."""
import json
import sys

import requests

import hook_messages

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
        response = requests.post(webhook['URL'],
                                 data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            print(
                f"Message sent '{webhook['TEAM_KANAL']}' successfully!")
        else:
            print(
                 "Failed to send message to "
                f"{webhook['TEAM_KANAL']}. Error: {response.text}")


if __name__ == "__main__":
    arguments = sys.argv[1]
    if arguments == "push":
        send_teams_message(webhook_dict,
                           "Es wurde etwas in den master gepusht"
                           )
    elif arguments == "release":
        send_teams_message(webhook_dict,
                           hook_messages.get_message(sys.argv[2], sys.argv[3])
                           )
    elif arguments == "delete":
        send_teams_message(webhook_dict,
                           "Löschen gemergerter Branches wurde durchgeführt"
                           )
    else:
        send_teams_message(webhook_dict,
                           "Das ist ein Test"
                           )
