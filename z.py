import requests
import json

def send_message_to_discord_webhook(webhook_url, message):
    if not webhook_url or not message:
        raise ValueError("Webhook URL and message cannot be empty")

    try:
        headers = {'Content-Type': 'application/json'}
        data = {'content': message}
        response = requests.post(webhook_url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        print(f"Message sent successfully to {webhook_url}")
    except requests.RequestException as e:
        print(f"Error sending message to {webhook_url}: {e}")

# Replace with your Discord webhook URL and message
webhook_url = "https://discord.com/api/webhooks/1238055168164102184/N2p3Tsb2ACw47yIPXBSJDmTUUVVZdp8YCkq9U9X7F2s--1GxKab1eLCtpDYXtTzHQpmM"
message = "123"

send_message_to_discord_webhook(webhook_url, message)