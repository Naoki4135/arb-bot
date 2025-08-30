import os

# 取引所
BYBIT_API_KEY = os.getenv('BYBIT_API_KEY', '')
BYBIT_SECRET_KEY = os.getenv('BYBIT_SECRET_KEY', '')
BITBANK_API_KEY = os.getenv('BITBANK_API_KEY', '')
BITBANK_SECRET_KEY = os.getenv('BITBANK_SECRET_KEY', '')

# 通知
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL', '')

# 監視シンボル
_default_bybit = os.getenv('SYMBOL_BYBIT', 'XLM/USDT')
_default_bitbank = os.getenv('SYMBOL_BITBANK', 'XLM/JPY')
_symbols_bybit_env = os.getenv('SYMBOLS_BYBIT')
_symbols_bitbank_env = os.getenv('SYMBOLS_BITBANK')

# 複数監視に対応（カンマ区切り）
SYMBOLS_BYBIT = [s.strip() for s in (
    _symbols_bybit_env or _default_bybit
).split(',') if s.strip()]
SYMBOLS_BITBANK = [s.strip() for s in (
    _symbols_bitbank_env or _default_bitbank
).split(',') if s.strip()]

# (base, bybit_symbol, bitbank_symbol) のタプル一覧
MONITOR_SYMBOLS = [
    (b.split('/')[0], b, bb)
    for b, bb in zip(SYMBOLS_BYBIT, SYMBOLS_BITBANK)
]

# 後方互換: 先頭要素を旧定数に保持
SYMBOL_BYBIT = SYMBOLS_BYBIT[0]
SYMBOL_BITBANK = SYMBOLS_BITBANK[0]

# 監視・通知パラメータ
ARBITRAGE_THRESHOLD_JPY = float(os.getenv('ARBITRAGE_THRESHOLD_JPY', '1.0'))
POLL_INTERVAL_SECONDS = float(os.getenv('POLL_INTERVAL_SECONDS', '5'))
NOTIFY_COOLDOWN_SECONDS = float(os.getenv('NOTIFY_COOLDOWN_SECONDS', '60'))
RENOTIFY_MIN_DELTA_JPY = float(os.getenv('RENOTIFY_MIN_DELTA_JPY', '0.5'))

# 為替
USE_DYNAMIC_USDTJPY = os.getenv('USE_DYNAMIC_USDTJPY', 'true').lower() == 'true'
FALLBACK_USDTJPY_RATE = float(os.getenv('FALLBACK_USDTJPY_RATE', '146.97'))

# 取引スイッチ
TRADE_ENABLED = os.getenv('TRADE_ENABLED', 'false').lower() == 'true'

# 取引パラメータ
MAX_NOTIONAL_JPY_PER_TRADE = float(os.getenv('MAX_NOTIONAL_JPY_PER_TRADE', '3000'))
SLIPPAGE_BPS = float(os.getenv('SLIPPAGE_BPS', '20'))  # 0.20%
TAKER_FEE_BYBIT = float(os.getenv('TAKER_FEE_BYBIT', '0.001'))     # 0.10%
TAKER_FEE_BITBANK = float(os.getenv('TAKER_FEE_BITBANK', '0.0015'))# 0.15%
MIN_PROFIT_JPY = float(os.getenv('MIN_PROFIT_JPY', '0.8'))
