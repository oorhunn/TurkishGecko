import datetime

from binance.client import Client
import json
import string


class BinanceService:
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
        lastfourteenday = str(tempyesterday - datetime.timedelta(days=13))
        lastsevenday = str(tempyesterday - datetime.timedelta(days=6))
        lastfourday = str(tempyesterday - datetime.timedelta(days=3))
        lasttwoday = str(tempyesterday - datetime.timedelta(days=1))
        yesterday = str(tempyesterday)

        dayklines = self.client.get_historical_klines(coin, Client.KLINE_INTERVAL_1DAY, lastfourteenday, yesterday)
        fourhourklines = self.client.get_historical_klines(coin, Client.KLINE_INTERVAL_4HOUR, lastsevenday, yesterday)
        hourlyklines = self.client.get_historical_klines(coin, Client.KLINE_INTERVAL_1HOUR, lastfourday, yesterday)
        fifteenminklines = self.client.get_historical_klines(coin, Client.KLINE_INTERVAL_15MINUTE, lasttwoday, yesterday)

        tempoutdata = {
            '14 Day Daily KLines': dayklines,
            '7 Day 4Hour KLines': fourhourklines,
            '4 Day 1Hour KLines': hourlyklines,
            '2 Day 15Min KLines': fifteenminklines
        }

        return tempoutdata


binance_service = BinanceService()
