import pandas as pd
from prophet import Prophet

def train_model(df):
    df = df.rename(columns={"date": "ds", "sales": "y"})
    model = Prophet()
    model.fit(df)
    return model

def predict(model, days):
    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)
    return forecast[['ds', 'yhat']]