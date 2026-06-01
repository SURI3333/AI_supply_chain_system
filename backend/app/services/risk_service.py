import pandas as pd
from app.ml.risk_model import train_risk, predict_risk
from app.utils.file_path import get_dataset_path

def get_risk():
    file_path = get_dataset_path("sample_inventory.csv")

    df = pd.read_csv(file_path)

    X = df[['sales']]
    y = (df['sales'] > df['sales'].mean()).astype(int)

    model = train_risk(X, y)

    risk = predict_risk(model, X)

    return risk