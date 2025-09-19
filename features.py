def add_features(df):
    df["rolling_mean"] = df["temperature"].rolling(window=10, min_periods=1).mean()
    df["rolling_std"] = df["temperature"].rolling(window=10, min_periods=1).std().fillna(0)
    df["z_score"] = (df["temperature"] - df["rolling_mean"]) / (df["rolling_std"] + 1e-5)
    return df
