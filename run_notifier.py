import time
from bot import settings
from bot.utils import now_str
from bot.orderbook import fetch_prices
from bot.rates import get_usdtjpy_rate
from bot.strategy import jpy_prices, notify_needed
from bot.notifier import send_discord

def main():
    print(f"[{now_str()}] Notifier開始（Docker）")
    last_at, last_diff = 0.0, None

    while True:
        t0 = time.time()
        prices = fetch_prices()
        if prices:
            usdtjpy = get_usdtjpy_rate()
            bybit_jpy, spread = jpy_prices(prices['bybit_ask_usdt'], usdtjpy, prices['bitbank_bid_jpy'])
            print(f"[{now_str()}] BYBIT(¥): {bybit_jpy:.4f}  BITBANK(¥): {prices['bitbank_bid_jpy']:.4f}  SPREAD: {spread:.4f}")
            ok, reason = notify_needed(spread, last_at, last_diff, t0)
            if ok:
                msg = (f"🚀 **裁定チャンス**\n"
                       f"SPREAD: `{spread:.4f} 円`\n"
                       f"Bybit(¥): `{bybit_jpy:.4f}` / bitbank(¥): `{prices['bitbank_bid_jpy']:.4f}`")
                send_discord(msg)
                last_at, last_diff = t0, spread
            else:
                print(f"[{now_str()}] 通知なし（{reason}）")
        time.sleep(max(0.0, settings.POLL_INTERVAL_SECONDS - (time.time()-t0)))

if __name__ == '__main__':
    main()
