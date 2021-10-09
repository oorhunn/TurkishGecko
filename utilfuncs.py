import json
import json
from config import Config
from binance.client import Client
import datetime
import string

def getcoindata(coin, interval, startdate):
    client = Client(Config.API_KEY, Config.API_SECRET)
    if interval == '1DAY':
        data = client.get_historical_klines(coin, Client.KLINE_INTERVAL_1DAY, startdate)
    elif interval == '4HOUR':
        data = client.get_historical_klines(coin, Client.KLINE_INTERVAL_4HOUR, startdate)
    elif interval == '1HOUR':
        data = client.get_historical_klines(coin, Client.KLINE_INTERVAL_1HOUR, startdate)
    elif interval == '15MIN':
        data = client.get_historical_klines(coin, Client.KLINE_INTERVAL_15MINUTE, startdate)
    else:
        return 'something went wrong'
    temp = startdate.translate({ord(c): None for c in string.whitespace})
    name = 'coindata/' + coin + str(interval) + str(temp[4:13]) + '.json'
    with open(name, '+w') as f:
        b = json.dumps(data, indent=4)
        f.write(b)
        f.close()

