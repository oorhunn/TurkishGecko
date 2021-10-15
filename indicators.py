import pandas as pd


# For calculating the Simple Moving Average (MA)
def MA(df, period, column='Close'):
    return df[column].rolling(window=period).mean()


