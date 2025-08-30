import requests  # HTTPリクエストを送るためのライブラリ
from . import settings  # 設定値を読み込む
from .utils import now_str  # ログ用の現在時刻取得

def send_discord(message: str):  # Discordへ通知を送る
    try:
        if not settings.DISCORD_WEBHOOK_URL:  # Webhookが設定されていない場合
            print(f"[{now_str()}] Webhook未設定: {message}")
            return
        r = requests.post(settings.DISCORD_WEBHOOK_URL, json={'content': message}, timeout=10)  # WebhookへPOST
        if r.status_code != 204:  # 成功ステータス以外なら
            print(f"[{now_str()}] Discord失敗 {r.status_code} {r.text[:200]}")
    except Exception as e:
        print(f"[{now_str()}] Discord例外: {e}")  # 例外発生時のログ

