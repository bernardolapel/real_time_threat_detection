from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import boto3, json

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

def extract_features():
    s3 = boto3.client('s3')
    logs = []
    for obj in s3.list_objects_v2(Bucket='cyber-threat-logs', Prefix='2025/')['Contents']:
        data = s3.get_object(Bucket='cyber-threat-logs', Key=obj['Key'])
        log = json.loads(data['Body'].read())
        logs.append(log)

    df = pd.DataFrame(logs)
    df['session_length'] = df['end_time'] - df['start_time']
    df['port_anomaly'] = df['dst_port'].apply(lambda p: 1 if p > 1024 else 0)
    df.to_csv('/tmp/feature_data.csv', index=False)

with DAG('feature_extraction_dag', default_args=default_args, schedule_interval='@hourly') as dag:
    extract_task = PythonOperator(task_id='extract_features', python_callable=extract_features)