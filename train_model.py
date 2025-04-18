import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

df = pd.read_csv('/tmp/feature_data.csv')
X = df[['session_length', 'port_anomaly']]

model = IsolationForest(contamination=0.01, random_state=42)
model.fit(X)

joblib.dump(model, 'model.joblib')