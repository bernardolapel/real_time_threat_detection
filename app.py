from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    X = np.array([[data['session_length'], data['port_anomaly']]])
    prediction = model.predict(X)[0]
    return jsonify({'threat_detected': int(prediction == -1)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)