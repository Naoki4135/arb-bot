import time, math  # 時間関連と数学関数

def now_str():  # 現在時刻を文字列で返す
    return time.strftime('%Y-%m-%d %H:%M:%S')

def safe_best_price(orderbook: dict, side: str):  # 板情報から最良気配値を安全に取得
    try:
        if side == 'ask':
            asks = orderbook.get('asks') or []  # 売り板を取り出す
            return asks[0][0] if asks else None  # 最上段の価格を返す
        if side == 'bid':
            bids = orderbook.get('bids') or []  # 買い板を取り出す
            return bids[0][0] if bids else None  # 最上段の価格を返す
    except Exception:
        return None  # 取得に失敗した場合
    return None  # 該当しない場合

def round_to(x, prec):  # 指定桁数に切り捨て
    if prec is None:
        return x  # 桁数指定が無い場合はそのまま
    f = 10 ** prec  # 10のべき乗を計算
    return math.floor(x * f) / f  # 指定桁で切り捨て

