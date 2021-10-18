import datetime
import pandas as pd
import json
from services.binance_service import binance_service


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
    df = pd.DataFrame(data)

    return df


# This class is doing preprocess, refactoring data for prophet applications
# It compares local data if local data is not up to date it updates data
class ProphetProcess:
    # TODO get_local_data function is currently under development
    # TODO my goal is to get local prophet data and then update it
    # TODO so when we are tried to run prophet code, it stayed up to date
    # def get_local_data(self, datapath):
    #     error = None
    #     df = pd.read_csv(datapath)
    #     df['Year'] = pd.DatetimeIndex(df['Open Time']).year
    #     df['Month'] = pd.DatetimeIndex(df['Open Time']).month
    #     df['Day'] = pd.DatetimeIndex(df['Open Time']).day
    #     lastdateyear = int(df['Year'].tail(1))
    #     lastdatemonth = int(df['Month'].tail(1))
    #     lastdateday = int(df['Day'].tail(1))
    #     now = datetime.datetime.utcnow()
    #     if lastdateyear == int(now.year):
    #         if lastdatemonth == int(now.month):
    #             if lastdateday >= int(now.day) - 1:
    #                 df.pop('Open Time')
    #                 # We do our calculations according to yesterdays values.
    #                 # -1 is for getting yesterdays values.
    #                 if lastdateday == int(now.day):
    #                     df.drop(index=df.index[-1], axis=0, inplace=True)
    #                     return df
    #                 else:
    #                     return df
    #             error = 'day needs an update'
    #             return error, lastdateday
    #         error = 'month needs an update'
    #         return error, lastdatemonth
    #     error = 'year needs an update'
    #     return error, lastdateyear

    def refactor_data(self, df):
        twoset = df.head(2)
        times = twoset['Open Time']
        difference = times[1] - times[0]
        if str(difference) == '1 days 00:00:00':
            nameout = prophet_service.name_returner(len(df), 'D')
        elif str(difference) == '0 days 04:00:00':
            nameout = prophet_service.name_returner(len(df), '4H')
        elif str(difference) == '0 days 01:00:00':
            nameout = prophet_service.name_returner(len(df), '1H')
        elif str(difference) == '0 days 00:15:00':
            nameout = prophet_service.name_returner(len(df), '15M')
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


prophet_service = ProphetProcess()

