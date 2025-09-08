from flask import Flask, Response, request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import Histogram
from time import sleep

app = Flask(__name__)

# Example metric: count HTTP requests
COUNT = Counter("app_requests_total", "Total number of requests")
HISTO = Histogram('request_latency_milliseconds', 'Description of histogram', buckets=[0.5, 1, 10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000, 30000])


@app.route("/increment")
def inc():
    COUNT.inc()
    return "Incremented"

@app.route("/latency/<observation>")
def histo(observation):
    HISTO.observe(int(observation))
    return "Observed " + observation

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route("/delay/<ms>")
def delay(ms):
    seconds = int(ms) / 1000
    sleep(seconds)
    return "Delayed " + ms
    
@app.route("/")
def index():
    return "Hello"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
