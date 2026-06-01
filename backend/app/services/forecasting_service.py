import pandas as pd
from app.ml.forecast_model import train_model, predict
from app.utils.file_path import get_dataset_path

def forecast_inventory(days):
    file_path = get_dataset_path("sample_inventory.csv")

    df = pd.read_csv(file_path)

    model = train_model(df)
    result = predict(model, days)

    return result.to_dict(orient="records")