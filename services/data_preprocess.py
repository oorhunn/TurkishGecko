import datetime
import pandas as pd
import json


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


