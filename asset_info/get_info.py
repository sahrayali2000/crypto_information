import ccxt
from crypto.models import Asset


def crypto_information():
    for coin in Asset.objects.all():
        coin_name = f'{coin.key}/USDT'
        kucoin = ccxt.kucoin()
        try:
            ohlcv = kucoin.fetch_ohlcv(coin_name, '1d', limit=2)
            price_today = ohlcv[1][-2]
            price_yesterday = ohlcv[0][-2]
            change = (price_today - price_yesterday) / price_yesterday * 100
            coin.change_percent = change
            coin.price = price_today
            coin.save()
        except:
            return 'No coin'