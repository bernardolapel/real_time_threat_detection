from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open('sample_logs.json') as f:
    logs = json.load(f)

for log in logs:
    producer.send('network-logs', log)
    time.sleep(1)