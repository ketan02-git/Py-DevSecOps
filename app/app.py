from flask import Flask, render_template
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from metrics import app_requests_total

app = Flask(__name__)

@app.route("/")
def home():
    app_requests_total.inc()
    return render_template("index.html")

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)