import pandas as pd
from sklearn.ensemble import IsolationForest




def detect(data):
    model = IsolationForest(contamination=0.05)

    data = data.copy()  # prevent modification issue

    data["anomaly"] = model.fit_predict(data)

    return data