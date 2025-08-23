from .utils import now_str
from . import settings
import ccxt

_SOURCES = [('bybit','USDT/JPY'), ('mexc','USDT/JPY'), ('binance','USDT/JPY')]
_clients = {}

def _client(exid):
    if exid in _clients: return _clients[exid]
    try:
        _clients[exid] = getattr(ccxt, exid)({'enableRateLimit': True})
    except Exception:
        _clients[exid] = None
    return _clients[exid]

def try_fetch_usdtjpy_rate():
    for exid, sym in _SOURCES:
        ex = _client(exid)
        if not ex: continue
        try:
            t = ex.fetch_ticker(sym)
            for k in ('last','bid','ask','close'):
                v = t.get(k)
                if isinstance(v, (int,float)) and v > 0:
                    return float(v)
        except Exception:
            continue
    return None

def get_usdtjpy_rate():
    if settings.USE_DYNAMIC_USDTJPY:
        r = try_fetch_usdtjpy_rate()
        if r and r > 0:
            return r
        print(f"[{now_str()}] 為替自動取得失敗。fallback {settings.FALLBACK_USDTJPY_RATE}")
    return settings.FALLBACK_USDTJPY_RATE

