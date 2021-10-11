import json
from config import Config
from binance.client import Client
import datetime
import string
import pandas as pd
import ta
from ta import add_all_ta_features
import utilfuncs
import indicators

# client = Client(Config.API_KEY, Config.API_SECRET)

# candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1MONTH)
# pastcandles = client.get_historical_klines("ETHUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2017")
# anan = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1HOUR)
# avg_price = client.get_avg_price(symbol='BTCUSDT')
# tickers = client.get_ticker()
#
# orders = client.get_all_orders(symbol='ADAUSDT')
# baban = client.get_historical_klines("ETHUSDT", Client.KLINE_INTERVAL_1DAY, "Fri, 01 Oct 2021 00:00:00 GMT")



datapath = 'coindata/preprocessed/ETHUSDT1DAY01Jan2017.csv'

df = pd.read_csv(datapath)
df['MA14'] = indicators.MA(df, period=14)
print(df)



