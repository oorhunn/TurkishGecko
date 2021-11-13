import datetime

from binance.client import Client
import json
import string
from config.constants import *


class BinanceService:
    def __init__(self, config=None):
        self.client = None
        self.Config = config

    def init_app(self, app):
        self.Config = app.config
        self.client = self._get_client()

    def _get_client(self):
        return Client(self.Config.get('API_KEY'), self.Config.get('API_SECRET'))

    def get_client(self):
        if not self.client:
            self.client = self._get_client()
        return self.client

    def get_coin_data(self, coin, interval, startdate):
        if not self.client:
            self.client = Client(self.Config.API_KEY, self.Config.API_SECRET)
        if interval == '1DAY':
            data = self.client.get_historical_klines(coin, Client.KLINE_INTERVAL_1DAY, startdate)
        elif interval == '4HOUR':
            data = self.client.get_historical_klines(coin, Client.KLINE_INTERVAL_4HOUR, startdate)
        elif interval == '1HOUR':
            data = self.client.get_historical_klines(coin, Client.KLINE_INTERVAL_1HOUR, startdate)
        elif interval == '15MIN':
            data = self.client.get_historical_klines(coin, Client.KLINE_INTERVAL_15MINUTE, startdate)
        else:
            return 'something went wrong'
        temp = startdate.translate({ord(c): None for c in string.whitespace})
        name = 'coindata/rawdata/' + coin + str(interval) + str(temp[4:13]) + '.json'
        with open(name, '+w') as f:
            b = json.dumps(data, indent=4)
            f.write(b)
            f.close()

    def get_prophet_data(self, coin):
        if not self.client:
            self.client = Client(self.Config.API_KEY, self.Config.API_SECRET)
        today = datetime.date.today()
        tempyesterday = today - datetime.timedelta(days=1)
        lastfourteenday = str(tempyesterday - datetime.timedelta(days=14))
        lastsevenday = str(tempyesterday - datetime.timedelta(days=7))
        lastfourday = str(tempyesterday - datetime.timedelta(days=4))
        lasttwoday = str(tempyesterday - datetime.timedelta(days=2))
        yesterday = str(tempyesterday)

        dayklines = self.client.get_historical_klines(
            symbol=coin, interval=Client.KLINE_INTERVAL_1DAY,
            start_str=lastfourteenday, end_str=yesterday, limit=WINDOW_DAY
        )
        fourhourklines = self.client.get_historical_klines(
            symbol=coin, interval=Client.KLINE_INTERVAL_4HOUR,
            start_str=lastsevenday, end_str=yesterday, limit=WINDOW_4H
        )
        hourlyklines = self.client.get_historical_klines(
            symbol=coin, interval=Client.KLINE_INTERVAL_1HOUR,
            start_str=lastfourday, end_str=yesterday, limit=WINDOW_1H
        )
        fifteenminklines = self.client.get_historical_klines(
            symbol=coin, interval=Client.KLINE_INTERVAL_15MINUTE,
            start_str=lasttwoday, end_str=yesterday, limit=WINDOW_15M
        )

        tempoutdata = {
            '14 Day Daily KLines': dayklines,
            '7 Day 4Hour KLines': fourhourklines,
            '4 Day 1Hour KLines': hourlyklines,
            '2 Day 15Min KLines': fifteenminklines
        }

        return tempoutdata


binance_service = BinanceService()
