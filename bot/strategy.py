from . import settings  # 設定値を参照

def jpy_ratio(bybit_ask_usdt, usdtjpy, bitbank_bid_jpy):  # 円建て価格と価格比を計算
    bybit_price_jpy = bybit_ask_usdt * usdtjpy  # BybitのUSDT建て価格を円換算
    ratio = bitbank_bid_jpy / bybit_price_jpy  # bitbank買い価格との比率を算出
    return bybit_price_jpy, ratio  # 円換算価格と価格比を返す


def notify_needed(ratio, last_notified_at, last_notified_ratio, now_ts):  # 通知が必要か判定
    if ratio < settings.ARBITRAGE_THRESHOLD_RATIO:  # 価格比がしきい値未満
        return False, "しきい値未達"
    if (now_ts - last_notified_at) < settings.NOTIFY_COOLDOWN_SECONDS:  # クールダウン期間内
        return False, "クールダウン中"
    if (last_notified_ratio is not None) and (
        abs(ratio - last_notified_ratio) < settings.RENOTIFY_MIN_DELTA_RATIO  # 再通知に必要な差分未満
    ):  # 変化が小さい
        return False, "変化小"
    return True, ""  # 通知必要
