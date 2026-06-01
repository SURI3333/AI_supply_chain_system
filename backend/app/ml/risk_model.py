from xgboost import XGBClassifier

def train_risk(X, y):
    model = XGBClassifier()
    model.fit(X, y)
    return model

def predict_risk(model, data):
    return model.predict_proba(data).tolist()