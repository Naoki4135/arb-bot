import time
from bot import settings
from bot.utils import now_str
from bot.orderbook import fetch_prices
from bot.rates import get_usdtjpy_rate
from bot.strategy import jpy_prices, notify_needed
from bot.notifier import send_discord


def main():
    print(f"[{now_str()}] Notifier開始（Docker）")
    last = {base: {'at': 0.0, 'diff': None}
            for base, _, _ in settings.MONITOR_SYMBOLS}

    while True:
        t0 = time.time()
        prices = fetch_prices()
        if prices:
            usdtjpy = get_usdtjpy_rate()
            for base, p in prices.items():
                bybit_jpy, spread = jpy_prices(
                    p['bybit_ask_usdt'], usdtjpy, p['bitbank_bid_jpy'])
                print(
                    f"[{now_str()}] {base} BYBIT(¥): {bybit_jpy:.4f}  "
                    f"BITBANK(¥): {p['bitbank_bid_jpy']:.4f}  SPREAD: {spread:.4f}"
                )
                info = last[base]
                ok, reason = notify_needed(spread, info['at'], info['diff'], t0)
                if ok:
                    msg = (
                        f"🚀 **裁定チャンス ({base})**\n"
                        f"SPREAD: `{spread:.4f} 円`\n"
                        f"Bybit(¥): `{bybit_jpy:.4f}` / bitbank(¥): `{p['bitbank_bid_jpy']:.4f}`"
                    )
                    send_discord(msg)
                    info['at'], info['diff'] = t0, spread
                else:
                    print(f"[{now_str()}] {base} 通知なし（{reason}）")
        time.sleep(max(0.0, settings.POLL_INTERVAL_SECONDS - (time.time() - t0)))


if __name__ == '__main__':
    main()

