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
import numpy as np
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

# df = pd.read_csv(datapath)
# df['MA14'] = indicators.MA(df, period=14)
# df['MA50'] = indicators.MA(df, period=50)
# df['MA200'] = indicators.MA(df, period=200)
# df['Signal1'] = np.where(df['MA14'] > df['MA50'], 1, 0)
# df['Signal2'] = np.where(df['MA14'] > df['MA200'], 1, 0)
# df['Signal3'] = np.where(df['MA50'] > df['MA200'], 1, 0)
# df['Postion1'] = df['Signal1'].diff()
# df['Postion2'] = df['Signal2'].diff()
# df['Postion3'] = df['Signal3'].diff()
#
#
# df['Buy1'] = np.where(df['Postion1'] == 1, df['Close'], np.NAN)
# df['Buy2'] = np.where(df['Postion2'] == 1, df['Close'], np.NAN)
#
# df['Sell1'] = np.where(df['Postion1'] == -1, df['Close'], np.NAN)
# df['Sell2'] = np.where(df['Postion2'] == -1, df['Close'], np.NAN)
#
# # df['Sell'] = np.where(df['Postion1'] == -1 or df['Postion2'] == -1 or df['Postion3'] == -1, df['Close'], np.NAN)
#
#
# plt.figure(figsize=(16, 8))
# plt.title('Close Price History w/ Sell & Buy Signals', fontsize=18)
# plt.plot(df['Close'], alpha=0.5, label='Close')
# plt.plot(df['MA14'], alpha=0.5, label='MA 14')
# plt.plot(df['MA50'], alpha=0.5, label='MA 50')
# plt.scatter(df.index, df['Buy1'], alpha=1, label='Buy Signal', marker='^', color='green')
# plt.scatter(df.index, df['Buy2'], alpha=1, label='Buy Signal', marker='^', color='green')
#
# plt.scatter(df.index, df['Sell1'], alpha=1, label='Sell Signal', marker='v', color='red')
# plt.scatter(df.index, df['Sell2'], alpha=1, label='Sell Signal', marker='v', color='red')
#
#
# plt.xlabel('Date', fontsize=18)
# plt.ylabel('Close Price', fontsize=18)
# plt.show()
df = pd.read_csv(datapath)


dftest = df.iloc[1513:, 1:]

dftrain = df.iloc[:1513, 1:]

# m.fit(df)
# future = m.make_future_dataframe(periods=365)
# future.tail()
# forecast = m.predict(future)
# forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()




