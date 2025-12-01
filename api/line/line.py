# api/line/line.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # .env を読み込む

def send_line_message(text: str):
    channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    user_id = os.getenv("LINE_USER_ID")

    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {channel_access_token}"
    }
    payload = {
        "to": user_id,
        "messages": [
            {"type": "text", "text": text}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    print("LINE API Response:", response.status_code, response.text)
    return response.status_code == 200
