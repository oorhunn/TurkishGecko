from datetime import date, datetime, timedelta
import pandas as pd
import json
from services.binance_service import BinanceService
from dateutil import parser
from services.utiltyfunctions import string_to_date_refactor
from config.constants import *
from config.local import *


class ProphetService:
    def __init__(self, bs):
        self.binance_service = bs

    @staticmethod
    def only_basic_pre_process(tempdata):
        Copentime = []
        Chigh = []
        Clow = []
        Copen = []
        Cclose = []
        Cvolume = []
        i = len(tempdata) - 1
        while i >= 0:
            dd = datetime.utcfromtimestamp(tempdata[i][0] / 1000)
            Copentime.append(dd)
            Copen.append(tempdata[i][1])
            Chigh.append(tempdata[i][2])
            Clow.append(tempdata[i][3])
            Cclose.append(tempdata[i][4])
            Cvolume.append(tempdata[i][5])
            i = i - 1
        data = {
            'Open Time': Copentime,
            'Open': Copen,
            'High': Chigh,
            'Low': Clow,
            'Close': Cclose,
            'Volume': Cvolume
        }
        df = pd.DataFrame(data)

        return df

    def check_local_data(self, filenamelist):
        not_usable_prophet_data = []
        for dat in filenamelist:
            month, day, year = string_to_date_refactor(dat)
            dateval = month + '/' + day + '/' + year
            local_file_date = (parser.parse(dateval)).date()
            today = datetime.today().date()
            if local_file_date != today:
                not_usable_prophet_data.append(dat)
                filenamelist.remove(dat)
        return filenamelist, not_usable_prophet_data

    @staticmethod
    def apply_windowing(df, _type, _range):
        data = {}
        for i in range(0, _range):
            try:
                data[f'{_type}_{i}'] = df[HIGH][i]
            except:
                break
        return pd.DataFrame(data, index=[0])

    def write_prophet_data(self, coin):
        day = datetime.now().day
        month = datetime.now().month
        year = datetime.now().year
        filename = 'coindata/preprocessed/prophetdata/' + str(coin) + ' ' + str(month) + '-' + str(day) + '-' + str(
            year) + '.csv'
        # result.to_csv(filename)

    def get_prophet_row(self, coin, today):
        # TODO:: write every row into a file
        daily, fourhour, onehour, fiftmins = self.get_time_fractal_dfs(coin, today)
        _1g = daily[[OPEN_TIME, HIGH]]
        _4s = self.apply_windowing(fourhour, '4H', WINDOW_4H)
        _1s = self.apply_windowing(onehour, '1H', WINDOW_1H)
        _15m = self.apply_windowing(fiftmins, '15M', WINDOW_15M)
        result = pd.concat([_1g, _4s, _1s, _15m], axis=1)
        return result

    def get_time_fractal_dfs(self, coin, today):
        client = self.binance_service.get_client()
        today = today - timedelta(days=1)
        lastsevenday = str(today - timedelta(days=7))
        lastfourday = str(today - timedelta(days=4))
        lasttwoday = str(today - timedelta(days=2))
        today = str(today)

        dayklines = client.get_historical_klines(
            symbol=coin, interval=client.KLINE_INTERVAL_1DAY,
            start_str=today, end_str=today, limit=WINDOW_DAY
        )
        fourhourklines = client.get_historical_klines(
            symbol=coin, interval=client.KLINE_INTERVAL_4HOUR,
            start_str=lastsevenday, end_str=today, limit=WINDOW_4H
        )
        hourlyklines = client.get_historical_klines(
            symbol=coin, interval=client.KLINE_INTERVAL_1HOUR,
            start_str=lastfourday, end_str=today, limit=WINDOW_1H
        )
        fifteenminklines = client.get_historical_klines(
            symbol=coin, interval=client.KLINE_INTERVAL_15MINUTE,
            start_str=lasttwoday, end_str=today, limit=WINDOW_15M
        )

        return self.only_basic_pre_process(dayklines), self.only_basic_pre_process(fourhourklines), \
            self.only_basic_pre_process(hourlyklines), self.only_basic_pre_process(fifteenminklines)


if __name__ == '__main__':
    coin = 'ETHUSDT'
    config = {'API_KEY': API_KEY, 'API_SECRET': API_SECRET}

    binance_service = BinanceService(config)
    prophet_service = ProphetService(binance_service)
    today = date.today()
    i = 0
    df_list = []
    while i < TOTAL_DAY_COUNT:
        df_list.append(prophet_service.get_prophet_row(coin, today))
        print(f'{today} icin satir hazirlandi!!')
        today = today - timedelta(days=1)
        i = i + 1
    df = pd.concat(df_list)
    print(df)