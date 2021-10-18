import json
from config import Config
from binance.client import Client
from datetime import datetime
import pandas as pd
import string
from services.data_preprocess import prophet_service
from config import Config
from services.binance_service import binance_service



datapath = 'coindata/preprocessed/ETHUSDT1DAY01Jan2017.csv'

# df = pd.read_csv(datapath)
# df['Year'] = pd.DatetimeIndex(df['Open Time']).year
#
# datanow = df['Open Time'].tail(1)
# now = datetime.utcnow()
# anan = df['Year'].tail(5)
# print(anan)

# df = prophet_service.get_local_data(datapath=datapath)
# if isinstance(df, pd.DataFrame):
#     print('aaa')
# else:
#     error, value = df

