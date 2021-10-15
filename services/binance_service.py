from binance.client import Client
from config import Config
import json
import string

class BinanceService():
    def init_app(self, Config):
        self.Config = Config
        self.client = Client(Config.API_KEY, Config.API_SECRET)

    def get_client(self):
        if not self.client:
            self.client = Client(self.Config.API_KEY, self.Config.API_SECRET)
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

    def prophet(self):
        return 'aa'
binance_service = BinanceService()
