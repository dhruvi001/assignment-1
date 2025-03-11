from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics  # Import Prometheus exporter

app = Flask(__name__)

# Initialize Prometheus metrics
metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    return "Welcome to the Flask Backend!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
