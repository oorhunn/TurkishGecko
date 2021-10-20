## Data
The data is in the coindata folder, we will use a csv file under examples folder

## Train a model
Initialize a prophet object:
```
m = Prophet()
```
Then, fit model:
```
m.fit(df)
```
Create a dataframe for predictions to fit in:
```
future = m.make_future_dataframe(periods=365)
```
Forecast:
```
forecast = m.predict(future)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
```