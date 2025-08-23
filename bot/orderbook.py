from . import settings
from .exchanges import bybit_public, bitbank_public
from .utils import safe_best_price, now_str

_bybit = bybit_public()
_bitbank = bitbank_public()

def fetch_prices():
    try:
        ob_bybit = _bybit.fetch_order_book(settings.SYMBOL_BYBIT)
        ob_bb = _bitbank.fetch_order_book(settings.SYMBOL_BITBANK)
        a = safe_best_price(ob_bybit, 'ask')
        b = safe_best_price(ob_bb, 'bid')
        if a is None or b is None:
            print(f"[{now_str()}] 板薄/取得失敗 a={a}, b={b}")
            return None
        return {"bybit_ask_usdt": float(a), "bitbank_bid_jpy": float(b)}
    except Exception as e:
        print(f"[{now_str()}] 価格取得例外: {e}")
        return None


