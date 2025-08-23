import requests
from . import settings
from .utils import now_str

def send_discord(message: str):
    try:
        if not settings.DISCORD_WEBHOOK_URL:
            print(f"[{now_str()}] Webhook未設定: {message}")
            return
        r = requests.post(settings.DISCORD_WEBHOOK_URL, json={'content': message}, timeout=10)
        if r.status_code != 204:
            print(f"[{now_str()}] Discord失敗 {r.status_code} {r.text[:200]}")
    except Exception as e:
        print(f"[{now_str()}] Discord例外: {e}")

