from prophet import Prophet
import pandas as pd

df = pd.read_csv('../coindata/examples/example_wp_log_peyton_manning.csv')
print(df.head())
print(df.count())

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=3)
print(future.tail())

forecast = m.predict(future)

print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
print(forecast.count())
