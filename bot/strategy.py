from . import settings

def jpy_prices(bybit_ask_usdt, usdtjpy, bitbank_bid_jpy):
    bybit_price_jpy = bybit_ask_usdt * usdtjpy
    spread = bitbank_bid_jpy - bybit_price_jpy
    return bybit_price_jpy, spread

def notify_needed(spread, last_notified_at, last_notified_diff, now_ts):
    if spread < settings.ARBITRAGE_THRESHOLD_JPY:
        return False, "しきい値未達"
    if (now_ts - last_notified_at) < settings.NOTIFY_COOLDOWN_SECONDS:
        return False, "クールダウン中"
    if (last_notified_diff is not None) and (abs(spread - last_notified_diff) < settings.RENOTIFY_MIN_DELTA_JPY):
        return False, "変化小"
    return True, ""

