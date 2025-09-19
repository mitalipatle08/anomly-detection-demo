from sklearn.ensemble import IsolationForest

def train_iforest(df, contamination=0.02):
    model = IsolationForest(contamination=contamination, random_state=42)
    df["anomaly"] = model.fit_predict(df[["temperature", "rolling_mean", "rolling_std", "z_score"]])
    return df, model
