"""
AI Model Training Script
Serverless AI Cloud Optimizer

This script trains a lightweight machine learning model
to predict cloud system risk based on monitoring metrics.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
import joblib


# -------------------------------
# Load Dataset
# -------------------------------
data = pd.read_csv("../data/sample_metrics.csv")

print("📊 Loaded Dataset:")
print(data.head())


# -------------------------------
# Feature Selection
# -------------------------------
features = ["cpu_usage", "memory_usage", "latency", "request_rate"]
X = data[features]


# -------------------------------
# Create Risk Labels (Simulated)
# -------------------------------
"""
Risk Label Logic:
0 -> Low Risk
1 -> High Risk

High risk is assumed when:
- CPU or Memory > 75%
- Latency > 250ms
"""

data["risk_label"] = np.where(
    (data["cpu_usage"] > 75) |
    (data["memory_usage"] > 75) |
    (data["latency"] > 250),
    1,
    0
)

y = data["risk_label"]

print("\n🧠 Generated Risk Labels:")
print(data[["cpu_usage", "memory_usage", "latency", "risk_label"]])


# -------------------------------
# Feature Scaling
# -------------------------------
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)


# -------------------------------
# Train AI Model
# -------------------------------
model = LogisticRegression()
model.fit(X_scaled, y)

print("\n✅ AI Model Training Complete")


# -------------------------------
# Save Model & Scaler
# -------------------------------
joblib.dump(model, "risk_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("💾 Model saved as 'risk_model.pkl'")
print("💾 Scaler saved as 'scaler.pkl'")
