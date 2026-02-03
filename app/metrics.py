from prometheus_client import Counter

app_requests_total = Counter(
    "flask_app_requests_total",
    "Total number of HTTP requests to Flask app"
)
