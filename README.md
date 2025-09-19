# IoT Sensor Anomaly Detection

This project demonstrates **anomaly detection** on IoT sensor data using **Isolation Forest**.  
The dataset is synthetic, with injected anomalies (spikes, drops, flatlines) to mimic real-world sensor failures.

---

## Workflow
1. Generate synthetic IoT sensor data (temperature readings).
2. Inject anomalies (spikes, sudden drops).
3. Train **Isolation Forest**.
4. Detect anomalies and visualize them.
5. Evaluate results using precision/recall against synthetic labels.

---
## Future Improvements
- Extend to **multi-sensor data** (vibration, humidity, battery).
- Try **Autoencoders** or **LSTMs** for time-series anomalies.
- Deploy anomaly detection as a **REST API** or stream job.

---

## How to Run
```bash
# Clone repo
git clone https://github.com/<your-username>/anomaly-detection-demo.git
cd anomaly-detection-demo

# Install dependencies
pip install -r requirements.txt

# Run notebook
jupyter notebook notebooks/anomaly_detection_demo.ipynb

