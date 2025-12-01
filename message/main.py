
# Channel情報
# Channel ID
# 2008574646
# Channel secret
# b31e2f2e6626c8eaea0a0a20318c8d46


# line_messaging.py
import requests
import json

CHANNEL_ACCESS_TOKEN = "ここにチャネルアクセストークン（長期）"
YOUR_USER_ID = "ここにあなたのユーザーID"

def send_message(message: str):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
    }
    payload = {
        "to": YOUR_USER_ID,
        "messages": [
            {"type": "text", "text": message}
        ]
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    
    print("LINE API Response:", r.status_code, r.text)
