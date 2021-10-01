import json
from config import Config
from binance.client import Client
import datetime

client = Client(Config.API_KEY, Config.API_SECRET)

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1MONTH)
anan = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1HOUR)
avg_price = client.get_avg_price(symbol='BTCUSDT')
tickers = client.get_ticker()
servertimereq = client.get_server_time()
servertime = servertimereq['serverTime']
orders = client.get_all_orders(symbol='ADAUSDT')
threhours = 3 * 60 * 1000
baban = servertime - threhours
systemstatus = client.get_system_status()

print(systemstatus)
print(type(systemstatus))
