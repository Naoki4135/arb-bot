from .utils import now_str  # 現在時刻の文字列化
from . import settings  # 設定値の取得
import ccxt  # 各取引所APIライブラリ
import requests  # HTTPリクエスト用ライブラリ

_SOURCES = [('bybit','USDT/JPY'), ('mexc','USDT/JPY'), ('binance','USDT/JPY')]  # ccxtで参照する取引所と通貨ペア
YAHOO_FINANCE_URL = 'https://query1.finance.yahoo.com/v7/finance/quote?symbols=USDJPY=X'  # YahooFinanceのUSDJPY取得URL

_clients = {}  # ccxtクライアントをキャッシュする辞書
_cached_rate = None  # 直近取得した為替レートのキャッシュ

def _client(exid):  # 取引所IDからccxtクライアントを取得
    if exid in _clients: return _clients[exid]  # 既存クライアントがあれば再利用
    try:
        _clients[exid] = getattr(ccxt, exid)({'enableRateLimit': True})  # 新規作成
    except Exception:
        _clients[exid] = None  # 作成失敗時はNone
    return _clients[exid]

def try_fetch_usdtjpy_rate():  # USDT/JPYレートの取得を試みる
    # first try ccxt exchanges
    for exid, sym in _SOURCES:  # 定義された取引所を順に試す
        ex = _client(exid)
        if not ex:
            continue  # クライアントが無ければスキップ
        try:
            t = ex.fetch_ticker(sym)  # ティッカー情報を取得
            for k in ('last', 'bid', 'ask', 'close'):  # 利用可能な価格フィールドを探す
                v = t.get(k)
                if isinstance(v, (int, float)) and v > 0:  # 正の数値なら採用
                    return float(v)
        except Exception:
            continue  # 失敗したら次へ

    # then try Yahoo Finance USD/JPY
    try:
        res = requests.get(YAHOO_FINANCE_URL, timeout=5)  # YahooFinanceから取得
        if res.ok:
            data = res.json()  # JSONデータを取得
            result = data.get('quoteResponse', {}).get('result', [])  # 結果配列を取り出す
            if result:
                v = result[0].get('regularMarketPrice')  # 現在価格を抽出
                if isinstance(v, (int, float)) and v > 0:  # 正の数値なら採用
                    return float(v)
    except Exception:
        pass  # 失敗したら次へ
    return None  # すべて失敗した場合

def get_usdtjpy_rate():  # USDT/JPYレートを取得する公開関数
    global _cached_rate
    if settings.USE_DYNAMIC_USDTJPY:  # 動的取得が有効な場合
        r = try_fetch_usdtjpy_rate()  # レート取得を試行
        if r and r > 0:  # 正常に取得できたら
            _cached_rate = r  # キャッシュを更新
            return r
        if _cached_rate:  # 以前の値があればそれを返す
            print(f"[{now_str()}] 為替自動取得失敗。cached {_cached_rate}")
            return _cached_rate
        print(
            f"[{now_str()}] 為替自動取得失敗。fallback {settings.FALLBACK_USDTJPY_RATE}"
        )
    return settings.FALLBACK_USDTJPY_RATE  # 動的取得しない場合や失敗時の値

