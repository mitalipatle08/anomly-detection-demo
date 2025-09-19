import pandas as pd
import numpy as np

def generate_sensor_data(n=1000, seed=42):
    np.random.seed(seed)
    time = pd.date_range("2023-01-01", periods=n, freq="H")
    temp = 25 + np.random.normal(0, 1, n)  # normal baseline

    # Inject anomalies
    temp[100:110] += 15   # spike
    temp[500:505] -= 10   # sudden drop
    temp[700:710] = 30    # flatline

    df = pd.DataFrame({"time": time, "temperature": temp})
    return df
