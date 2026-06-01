import pandas as pd
from app.ml.anomaly_model import detect
from app.utils.file_path import get_dataset_path

def get_anomalies():
    file_path = get_dataset_path("sample_inventory.csv")

    df = pd.read_csv(file_path)

    result = detect(df[['sales']])

    return result.to_dict(orient="records")