from prometheus_client import start_http_server, Gauge
import time
import random

inference_latency = Gauge('inference_latency_seconds', 'Time spent processing prediction')

def simulate_latency():
    while True:
        latency = random.uniform(0.05, 0.3)
        inference_latency.set(latency)
        time.sleep(5)

if __name__ == '__main__':
    start_http_server(8000)
    simulate_latency()