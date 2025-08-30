import time  # 時間操作のための標準ライブラリ
from bot import settings  # 設定値を読み込む
from bot.utils import now_str  # 現在時刻文字列を得る関数
from bot.orderbook import fetch_prices  # 板情報を取得する関数
from bot.rates import get_usdtjpy_rate  # 為替レート取得関数
from bot.strategy import jpy_prices, notify_needed  # 価格計算と通知条件判定
from bot.notifier import send_discord  # Discord通知送信関数


def main():  # メインループ
    print(f"[{now_str()}] Notifier開始（Docker）")  # 起動ログを出力
    last = {base: {'at': 0.0, 'diff': None}  # 各通貨の最終通知時刻とスプレッドを保持
            for base, _, _ in settings.MONITOR_SYMBOLS}

    while True:  # 永久ループで監視
        t0 = time.time()  # ループ開始時刻
        prices = fetch_prices()  # 各取引所から価格を取得
        if prices:  # 価格が取得できた場合
            usdtjpy = get_usdtjpy_rate()  # USDT/JPYレートを取得
            for base, p in prices.items():  # 通貨ごとに処理
                bybit_jpy, spread = jpy_prices(
                    p['bybit_ask_usdt'], usdtjpy, p['bitbank_bid_jpy'])  # 円建て価格とスプレッド計算
                print(
                    f"[{now_str()}] {base} BYBIT(¥): {bybit_jpy:.4f}  "
                    f"BITBANK(¥): {p['bitbank_bid_jpy']:.4f}  SPREAD: {spread:.4f}"
                )  # 取得した価格をログ出力
                info = last[base]  # 直近通知情報を取り出す
                ok, reason = notify_needed(spread, info['at'], info['diff'], t0)  # 通知が必要か判定
                if ok:  # 通知すべきなら
                    msg = (
                        f"🚀 **裁定チャンス ({base})**\n"  # 通知メッセージ作成
                        f"SPREAD: `{spread:.4f} 円`\n"
                        f"Bybit(¥): `{bybit_jpy:.4f}` / bitbank(¥): `{p['bitbank_bid_jpy']:.4f}`"
                    )
                    send_discord(msg)  # Discordへ送信
                    info['at'], info['diff'] = t0, spread  # 通知情報を更新
                else:  # 通知不要の場合
                    print(f"[{now_str()}] {base} 通知なし（{reason}）")  # 理由をログ出力
        time.sleep(max(0.0, settings.POLL_INTERVAL_SECONDS - (time.time() - t0)))  # インターバル調整


if __name__ == '__main__':  # スクリプトが直接実行されたとき
    main()  # メイン関数を呼び出す

