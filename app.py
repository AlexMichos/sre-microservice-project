import time
import random
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Αρχικοποίηση του Prometheus Metrics Exporter
metrics = PrometheusMetrics(app)

# Προσθήκη στατικών πληροφοριών για την εφαρμογή (App Info metric)
metrics.info('app_info', 'Application info', version='1.0.0')

@app.route('/')
def home():
    time.sleep(random.uniform(0.05, 0.2))
    return jsonify({
        "status": "success",
        "message": "Welcome to the SRE Demo Microservice!"
    }), 200

@app.route('/health')
def health():
    return jsonify({"status": "UP"}), 200

@app.route('/simulate-error')
def simulate_error():
    return jsonify({"status": "error", "message": "Internal Server Error simulated!"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)