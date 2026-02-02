# Serverless AI Cloud Optimizer

An AI-powered, serverless cloud optimization system that uses event-driven intelligence to predict risk and optimize cloud resources without always-on servers.

---

## 📌 Problem Statement

Traditional cloud optimization systems rely on continuously running servers and static threshold-based rules.  
This leads to:
- High idle infrastructure costs  
- Reactive scaling instead of proactive decisions  
- Inefficient cloud resource utilization  

There is a need for a cost-efficient, intelligent, and event-driven cloud optimization approach.

---

## 💡 Proposed Solution

This project implements a **serverless AI-based cloud optimization system** where:

- Cloud monitoring metrics trigger events  
- A serverless function executes only when required  
- A lightweight AI model analyzes system metrics  
- Intelligent optimization decisions are generated  
- The function terminates immediately after execution  

This design ensures efficient cloud resource usage with **zero idle compute cost**.

---

## 🏗️ System Architecture

The system follows an event-driven serverless architecture:

1. Cloud monitoring metrics trigger an event  
2. A serverless function is invoked  
3. The AI model evaluates system risk  
4. Optimization actions are suggested or executed  
5. The function terminates after completion  

📌 Refer to the architecture diagram available in the `architecture/` directory.

---

## ⚙️ Tech Stack

- **Programming Language:** Python  
- **Cloud Architecture:** Serverless Computing  
- **AI / Machine Learning:** Scikit-learn  
- **Data Processing:** Pandas, NumPy  
- **Monitoring Data:** Simulated cloud metrics  

---

## ✨ Key Features

- Event-driven serverless execution  
- AI-based decision making  
- Cost-efficient cloud optimization  
- No always-on backend servers  
- Explainable optimization decisions  

---

## 🧠 AI Model Overview

A lightweight machine learning model is used to analyze cloud metrics such as:
- CPU usage  
- Memory usage  
- Network latency  
- Request rate  

The model predicts a **risk score** representing the likelihood of system overload or inefficient resource usage.  
Based on this score, optimization decisions are generated.

📌 Model training logic is available in the `ai-model/` directory.

---

## 📊 Sample Input Metrics

The system works on cloud metrics in the following format:

