from flask import Flask, Response, request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import Histogram
from time import sleep

app = Flask(__name__)

# Example metric: count HTTP requests
REQUEST_COUNT = Counter("app_requests_total", "Total number of requests")
HISTO = Histogram('request_latency_seconds', 'Description of histogram')


@app.route("/")
def index():
    REQUEST_COUNT.inc()
    HISTO.observe(4.7)    # Observe 4.7 (seconds in this case)
    return "Hello, Prometheus!"


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route("/delay/<ms>")
def delay(ms):
    seconds = int(ms) / 1000
    sleep(seconds)
    return "Hello"
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
