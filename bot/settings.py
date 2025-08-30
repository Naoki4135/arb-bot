import os  # OS関連の機能を利用するための標準ライブラリを読み込む

# 取引所
BYBIT_API_KEY = os.getenv('BYBIT_API_KEY', '')  # BybitのAPIキーを環境変数から取得
BYBIT_SECRET_KEY = os.getenv('BYBIT_SECRET_KEY', '')  # Bybitのシークレットキーを取得
BITBANK_API_KEY = os.getenv('BITBANK_API_KEY', '')  # bitbankのAPIキーを環境変数から取得
BITBANK_SECRET_KEY = os.getenv('BITBANK_SECRET_KEY', '')  # bitbankのシークレットキーを取得

# 通知
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL', '')  # Discord通知用Webhook URL

# 監視シンボル
_default_bybit = os.getenv('SYMBOL_BYBIT', 'XLM/USDT')  # Bybit用デフォルトシンボル
_default_bitbank = os.getenv('SYMBOL_BITBANK', 'XLM/JPY')  # bitbank用デフォルトシンボル
_symbols_bybit_env = os.getenv('SYMBOLS_BYBIT')  # 複数指定されたBybitシンボル
_symbols_bitbank_env = os.getenv('SYMBOLS_BITBANK')  # 複数指定されたbitbankシンボル

# 複数監視に対応（カンマ区切り）
SYMBOLS_BYBIT = [s.strip() for s in (  # Bybitシンボルの一覧を生成
    _symbols_bybit_env or _default_bybit  # 環境変数が無ければデフォルト値を使用
).split(',') if s.strip()]  # カンマで分割し空白を除去
SYMBOLS_BITBANK = [s.strip() for s in (  # bitbankシンボルの一覧を生成
    _symbols_bitbank_env or _default_bitbank  # 環境変数が無ければデフォルト値を使用
).split(',') if s.strip()]  # カンマで分割し空白を除去

# (base, bybit_symbol, bitbank_symbol) のタプル一覧
MONITOR_SYMBOLS = [  # 監視対象通貨ごとのシンボル対応リスト
    (b.split('/')[0], b, bb)  # 通貨名と各取引所のシンボルをタプル化
    for b, bb in zip(SYMBOLS_BYBIT, SYMBOLS_BITBANK)  # Bybitとbitbankのシンボルをペアにする
]

# 後方互換: 先頭要素を旧定数に保持
SYMBOL_BYBIT = SYMBOLS_BYBIT[0]  # 既存コードとの互換のため最初のシンボルを保持
SYMBOL_BITBANK = SYMBOLS_BITBANK[0]  # 同上、bitbank用

# 監視・通知パラメータ
ARBITRAGE_THRESHOLD_RATIO = float(os.getenv('ARBITRAGE_THRESHOLD_RATIO', '1.01'))  # 通知を行う価格比の閾値
POLL_INTERVAL_SECONDS = float(os.getenv('POLL_INTERVAL_SECONDS', '5'))  # 価格取得の間隔秒数
NOTIFY_COOLDOWN_SECONDS = float(os.getenv('NOTIFY_COOLDOWN_SECONDS', '60'))  # 通知後のクールダウン秒数
RENOTIFY_MIN_DELTA_RATIO = float(os.getenv('RENOTIFY_MIN_DELTA_RATIO', '0.01'))  # 再通知に必要な比率差


# 為替
USE_DYNAMIC_USDTJPY = os.getenv('USE_DYNAMIC_USDTJPY', 'true').lower() == 'true'  # 為替を動的取得するか
FALLBACK_USDTJPY_RATE = float(os.getenv('FALLBACK_USDTJPY_RATE', '146.97'))  # 為替取得失敗時のデフォルトレート

# 取引スイッチ
TRADE_ENABLED = os.getenv('TRADE_ENABLED', 'false').lower() == 'true'  # 実際の取引を行うかどうか

# 取引パラメータ
MAX_NOTIONAL_JPY_PER_TRADE = float(os.getenv('MAX_NOTIONAL_JPY_PER_TRADE', '3000'))  # 1回の取引での最大想定額
SLIPPAGE_BPS = float(os.getenv('SLIPPAGE_BPS', '20'))  # 想定スリッページをベーシスポイントで設定
TAKER_FEE_BYBIT = float(os.getenv('TAKER_FEE_BYBIT', '0.001'))     # Bybitのテイカー手数料
TAKER_FEE_BITBANK = float(os.getenv('TAKER_FEE_BITBANK', '0.0015'))# bitbankのテイカー手数料
MIN_PROFIT_JPY = float(os.getenv('MIN_PROFIT_JPY', '0.8'))  # 取引を行う最小利益額
