import ccxt

def bybit_public():
    """公開APIだけ使うBybitクライアント（監視用）"""
    return ccxt.bybit({'enableRateLimit': True})

def bitbank_public():
    """公開APIだけ使うbitbankクライアント（監視用）"""
    return ccxt.bitbank({'enableRateLimit': True})
import ccxt
from . import settings

def bybit_client(with_keys: bool):
    base = {'enableRateLimit': True}
    if with_keys and settings.TRADE_ENABLED and settings.BYBIT_API_KEY and settings.BYBIT_SECRET_KEY:
        base.update({'apiKey': settings.BYBIT_API_KEY, 'secret': settings.BYBIT_SECRET_KEY})
    return ccxt.bybit(base)

def bitbank_client(with_keys: bool):
    base = {'enableRateLimit': True}
    if with_keys and settings.TRADE_ENABLED and settings.BITBANK_API_KEY and settings.BITBANK_SECRET_KEY:
        base.update({'apiKey': settings.BITBANK_API_KEY, 'secret': settings.BITBANK_SECRET_KEY})
    return ccxt.bitbank(base)

