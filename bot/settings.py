import os

# 取引所
BYBIT_API_KEY = os.getenv('BYBIT_API_KEY', '')
BYBIT_SECRET_KEY = os.getenv('BYBIT_SECRET_KEY', '')
BITBANK_API_KEY = os.getenv('BITBANK_API_KEY', '')
BITBANK_SECRET_KEY = os.getenv('BITBANK_SECRET_KEY', '')

# 通知
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL', '')

# 監視シンボル
SYMBOL_BYBIT = os.getenv('SYMBOL_BYBIT', 'XLM/USDT')
SYMBOL_BITBANK = os.getenv('SYMBOL_BITBANK', 'XLM/JPY')

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
