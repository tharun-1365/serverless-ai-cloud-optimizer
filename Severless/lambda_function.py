"""
Serverless AI Cloud Optimizer - Lambda Function

This file simulates an AWS Lambda (serverless) function that:
1. Receives cloud metrics
2. Uses an AI-based risk evaluation
3. Makes an optimization decision
"""

import numpy as np


# -------------------------------
# Simulated AI Risk Prediction
# -------------------------------
def predict_risk(cpu, memory, latency, request_rate):
    """
    Simulates an AI model that predicts system risk.
    Output: risk score between 0 and 1
    """

    # Normalize inputs
    cpu_norm = cpu / 100
    memory_norm = memory / 100
    latency_norm = min(latency / 500, 1)       # cap latency
    request_norm = min(request_rate / 1000, 1) # cap requests

    # Weighted risk calculation (acts like a lightweight ML model)
    risk_score = (
        0.35 * cpu_norm +
        0.30 * memory_norm +
        0.20 * latency_norm +
        0.15 * request_norm
    )

    return round(risk_score, 2)


# -------------------------------
# Optimization Decision Logic
# -------------------------------
def optimization_decision(risk_score):
    """
    Determines action based on predicted risk score
    """

    if risk_score >= 0.75:
        return "SCALE UP resources (High Risk Detected)"
    elif risk_score >= 0.45:
        return "MONITOR closely (Moderate Risk)"
    else:
        return "NO ACTION required (System Healthy)"


# -------------------------------
# Lambda Handler (Entry Point)
# -------------------------------
def lambda_handler(event=None, context=None):
    """
    Simulated AWS Lambda handler
    """

    # Sample cloud metrics (simulated input)
    metrics = {
        "cpu_usage": 78,        # %
        "memory_usage": 82,     # %
        "latency": 240,         # ms
        "request_rate": 620     # requests/min
    }

    print("📥 Received Cloud Metrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")

    # Predict risk using AI logic
    risk = predict_risk(
        metrics["cpu_usage"],
        metrics["memory_usage"],
        metrics["latency"],
        metrics["request_rate"]
    )

    # Decide optimization action
    decision = optimization_decision(risk)

    # Output result
    response = {
        "risk_score": risk,
        "decision": decision
    }

    print("\n🤖 AI Risk Analysis:")
    print(f"  Risk Score: {risk}")
    print(f"  Decision : {decision}")

    return response


# -------------------------------
# Local Testing
# -------------------------------
if __name__ == "__main__":
    print("🚀 Running Serverless AI Cloud Optimizer locally...\n")
    lambda_handler()
