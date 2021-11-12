from datetime import datetime
import pandas as pd
import json
from services.binance_service import binance_service
from dateutil import parser
from services.utiltyfunctions import string_to_date_refactor



# This function is used for basic simplification of KLine data
# It`s saves Open Time, Open, High, Low, Close, Volume in pandas dataframe as .csv file in coindata/preprocessed/
def basic_preprocess(file):
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
        dd = datetime.utcfromtimestamp(tempdata[i][0] / 1000)
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


def haikin_average(openval, close, high, low):
    # Just to be sure
    openval = float(openval)
    close = float(close)
    high = float(high)
    low = float(low)
    average = (openval + close + high + low) / 4
    return average


def only_basic_pre_process(tempdata):
    Copentime = []
    Chigh = []
    Clow = []
    Copen = []
    Cclose = []
    Cvolume = []
    i = 0
    while i < len(tempdata):
        dd = datetime.utcfromtimestamp(tempdata[i][0] / 1000)
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
    df = pd.DataFrame(data)

    return df


# This class is doing preprocess, refactoring data for prophet applications
# It compares local data if local data is not up to date it updates data
class ProphetProcess:
    # TODO get_local_data function is currently under development
    # TODO my goal is to get local prophet data and then update it
    # TODO so when we are tried to run prophet code, it stayed up to date
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

    def refactor_data(self, df):
        twoset = df.head(2)
        times = twoset['Open Time']
        difference = times[1] - times[0]
        if str(difference) == '1 days 00:00:00':
            nameout = prophet_service.name_returner(len(df), 'D')
        elif str(difference) == '0 days 04:00:00':
            nameout = prophet_service.name_returner(len(df), '4H')
            df['Volume'] = None
        elif str(difference) == '0 days 01:00:00':
            nameout = prophet_service.name_returner(len(df), '1H')
            df['Volume'] = None

        elif str(difference) == '0 days 00:15:00':
            nameout = prophet_service.name_returner(len(df), '15M')
            df['Volume'] = None

        else:
            nameout = None
        if nameout is not None:
            df['Name'] = nameout
        openS = df['Open']
        closeS = df['Close']
        highS = df['High']
        lowS = df['Low']
        count = 0
        average = []
        while count < len(df):
            average.append(haikin_average(openS[count], closeS[count], highS[count], lowS[count]))
            count = count + 1
        df['Haiking Average'] = average

    def name_returner(self, length, char):
        empty = []
        i = 0
        while i < length:
            name = char + str(length - i)
            empty.append(name)
            i = i + 1
        return empty

    @staticmethod
    def _get_highest(df):
        return df['High']

    def get_prophet_data(self, coin):
        tempdata = binance_service.get_prophet_data(coin)
        daily = only_basic_pre_process(tempdata['14 Day Daily KLines'])
        fourhour = only_basic_pre_process(tempdata['7 Day 4Hour KLines'])
        onehour = only_basic_pre_process(tempdata['4 Day 1Hour KLines'])
        fiftmins = only_basic_pre_process(tempdata['2 Day 15Min KLines'])

        # [ds, y, 4s...., 1s..., 15d....]
        # highest

        # prophet_service.refactor_data(daily)
        # prophet_service.refactor_data(fourhour)
        # prophet_service.refactor_data(onehour)
        # prophet_service.refactor_data(fiftmins)
        _1g = daily[['Open Time', 'High']]
        _4s = self._get_highest(fourhour)
        _1s = self._get_highest(onehour)
        _15m = self._get_highest(fiftmins)
        result = pd.concat([_1g, _4s, _1s, _15m], axis=1)
        day = datetime.now().day
        month = datetime.now().month
        year = datetime.now().year
        filename = 'coindata/preprocessed/prophetdata/' + str(coin) + ' ' + str(month) + '-' + str(day) + '-' + str(year) + '.csv'
        result.to_csv(filename)

prophet_service = ProphetProcess()

