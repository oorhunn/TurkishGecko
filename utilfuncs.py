import json
from config import Config
from binance.client import Client
import datetime
import string
import pandas as pd


# For getting KLine data from binance.api
def GetCoinData(coin, interval, startdate):
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
    name = 'coindata/rawdata/' + coin + str(interval) + str(temp[4:13]) + '.json'
    with open(name, '+w') as f:
        b = json.dumps(data, indent=4)
        f.write(b)
        f.close()


# This function is used for basic simplification of KLine data
# It`s saves Open Time, Open, High, Low, Close, Volume in pandas dataframe as .csv file in coindata/preprocessed/
def BasicPreprocess(file):
    temp = open(file)
    tempdata = json.load(temp)
    Copentime = []
    Chigh = []
    Clow = []
    Copen = []
    Cclose = []
    Cvolume = []
    i = 0
    while i < len(tempdata):
        dd = datetime.datetime.utcfromtimestamp(tempdata[i][0] / 1000)
        Copentime.append(dd)
        Copen.append(tempdata[i][1])
        Chigh.append(tempdata[i][2])
        Clow.append(tempdata[i][3])
        Cclose.append(tempdata[i][4])
        Cvolume.append(tempdata[i][5])
        i = i + 1
    data = {
        'Open Time': Copentime,
        'Open': Copen,
        'High': Chigh,
        'Low': Clow,
        'Close': Cclose,
        'Volume': Cvolume
    }
    del tempdata
    df = pd.DataFrame(data)
    tempnameA = file.strip('coindata/rawdata/')
    tempnameB = 'coindata/preprocessed/' + tempnameA.strip('.json') + '.csv'
    df.to_csv(tempnameB)


