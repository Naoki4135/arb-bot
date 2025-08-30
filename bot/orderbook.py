from . import settings
from .exchanges import bybit_public, bitbank_public
from .utils import safe_best_price, now_str

_bybit = bybit_public()
_bitbank = bitbank_public()

def fetch_prices():
    results = {}
    for base, sym_bybit, sym_bb in settings.MONITOR_SYMBOLS:
        try:
            ob_bybit = _bybit.fetch_order_book(sym_bybit)
            ob_bb = _bitbank.fetch_order_book(sym_bb)
            a = safe_best_price(ob_bybit, 'ask')
            b = safe_best_price(ob_bb, 'bid')
            if a is None or b is None:
                print(f"[{now_str()}] {base} 板薄/取得失敗 a={a}, b={b}")
                continue
            results[base] = {"bybit_ask_usdt": float(a), "bitbank_bid_jpy": float(b)}
        except Exception as e:
            print(f"[{now_str()}] {base} 価格取得例外: {e}")
    return results


