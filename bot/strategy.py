from . import settings  # 設定値を参照

def jpy_prices(bybit_ask_usdt, usdtjpy, bitbank_bid_jpy):  # 円建て価格とスプレッド計算
    bybit_price_jpy = bybit_ask_usdt * usdtjpy  # BybitのUSDT建て価格を円換算
    spread = bitbank_bid_jpy - bybit_price_jpy  # bitbank買い価格との差
    return bybit_price_jpy, spread

def notify_needed(spread, last_notified_at, last_notified_diff, now_ts):  # 通知が必要か判定
    if spread < settings.ARBITRAGE_THRESHOLD_JPY:  # 利ざやがしきい値未満
        return False, "しきい値未達"
    if (now_ts - last_notified_at) < settings.NOTIFY_COOLDOWN_SECONDS:  # クールダウン期間内
        return False, "クールダウン中"
    if (last_notified_diff is not None) and (abs(spread - last_notified_diff) < settings.RENOTIFY_MIN_DELTA_JPY):  # 変化が小さい
        return False, "変化小"
    return True, ""  # 通知必要

