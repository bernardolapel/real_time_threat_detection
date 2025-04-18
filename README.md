# Real-Time Threat Detection System

This project implements an end-to-end real-time cybersecurity threat detection system using Kafka, Bash, Airflow, SageMaker, Docker, and Kubernetes.

## Components
- Kafka Producer & Consumer
- Feature Extraction DAG with Airflow
- Model Training (Scikit-learn)
- Real-time Inference API (Flask)
- Docker & Kubernetes Deployment
- Prometheus Monitoring

## Setup Instructions
1. Start Kafka and Zookeeper locally.
2. Run the Kafka producer and consumer scripts.
3. Use Airflow to schedule the feature extraction DAG.
4. Train the model and deploy it via Flask API.
5. Containerize the app using Docker and deploy on Kubernetes.
6. Monitor system metrics with Prometheus.