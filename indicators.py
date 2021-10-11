import pandas as pd


# For calculating the Simple Moving Average (MA)
def MA(data, period, column='Close'):
    return data[column].rolling(window=period).mean()


