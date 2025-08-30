from . import settings  # 設定値を読み込む
from .exchanges import bybit_public, bitbank_public  # 取引所APIクライアント生成関数
from .utils import safe_best_price, now_str  # 補助関数のインポート


_bybit = bybit_public()  # Bybitの公開APIクライアント
_bitbank = bitbank_public()  # bitbankの公開APIクライアント

def fetch_prices():  # 各取引所から価格を取得する
    results = {}  # 取得した価格を格納する辞書
    for base, sym_bybit, sym_bb in settings.MONITOR_SYMBOLS:  # 各監視対象通貨をループ
        try:
            ob_bybit = _bybit.fetch_order_book(sym_bybit)  # Bybitの板情報を取得
            ob_bb = _bitbank.fetch_order_book(sym_bb)  # bitbankの板情報を取得
            a = safe_best_price(ob_bybit, 'ask')  # Bybitの最良売り価格を取得
            b = safe_best_price(ob_bb, 'bid')  # bitbankの最良買い価格を取得
            if a is None or b is None:  # どちらか取得できなければ
                print(f"[{now_str()}] {base} 板薄/取得失敗 a={a}, b={b}")  # エラーメッセージを表示
                continue  # 次の通貨へ
            results[base] = {"bybit_ask_usdt": float(a), "bitbank_bid_jpy": float(b)}  # 結果を保存
        except Exception as e:
            print(f"[{now_str()}] {base} 価格取得例外: {e}")  # 例外時のログ
    return results  # 取得結果を返す