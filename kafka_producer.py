from kafka import KafkaProducer
import json
import time
import requests

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

url = "https://malicious-scanner.p.rapidapi.com/rapid/url"
querystring = {"url": "https://vryjm.page.link/jS6a"}

headers = {
    "x-rapidapi-key": "ba2dada015msh3dee5ece6fdb97fp128156jsn811fe85679fa",
    "x-rapidapi-host": "malicious-scanner.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
#print(response.json())

with open('response.json') as f:
    res = json.load(f)

for r in res:
    producer.send('mal_response', r)
    time.sleep(1)
