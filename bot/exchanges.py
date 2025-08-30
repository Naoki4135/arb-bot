import ccxt  # 複数取引所のAPIを扱うライブラリ

def bybit_public():
    """公開APIだけ使うBybitクライアント（監視用）"""
    return ccxt.bybit({'enableRateLimit': True})  # レート制限対応のBybitクライアント

def bitbank_public():
    """公開APIだけ使うbitbankクライアント（監視用）"""
    return ccxt.bitbank({'enableRateLimit': True})  # レート制限対応のbitbankクライアント
import ccxt  # 上記で既にインポートしているが再掲（互換性維持）
from . import settings  # 設定値を参照

def bybit_client(with_keys: bool):  # Bybitクライアントを作成
    base = {'enableRateLimit': True}  # レート制限を有効化
    if with_keys and settings.TRADE_ENABLED and settings.BYBIT_API_KEY and settings.BYBIT_SECRET_KEY:
        base.update({'apiKey': settings.BYBIT_API_KEY, 'secret': settings.BYBIT_SECRET_KEY})  # 認証情報を設定
    return ccxt.bybit(base)

def bitbank_client(with_keys: bool):  # bitbankクライアントを作成
    base = {'enableRateLimit': True}  # レート制限を有効化
    if with_keys and settings.TRADE_ENABLED and settings.BITBANK_API_KEY and settings.BITBANK_SECRET_KEY:
        base.update({'apiKey': settings.BITBANK_API_KEY, 'secret': settings.BITBANK_SECRET_KEY})  # 認証情報を設定
    return ccxt.bitbank(base)

