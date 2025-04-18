from kafka import KafkaConsumer
import json
import boto3

consumer = KafkaConsumer(
    'network-logs',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

s3 = boto3.client('s3')

for message in consumer:
    record = message.value
    record['timestamp'] = int(record['timestamp'].split('.')[0])
    s3.put_object(Bucket='cyber-threat-logs', Key=f"{record['timestamp']}.json", Body=json.dumps(record))