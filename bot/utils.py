import time, math

def now_str():
    return time.strftime('%Y-%m-%d %H:%M:%S')

def safe_best_price(orderbook: dict, side: str):
    try:
        if side == 'ask':
            asks = orderbook.get('asks') or []
            return asks[0][0] if asks else None
        if side == 'bid':
            bids = orderbook.get('bids') or []
            return bids[0][0] if bids else None
    except Exception:
        return None
    return None

def round_to(x, prec):
    if prec is None:
        return x
    f = 10 ** prec
    return math.floor(x * f) / f

