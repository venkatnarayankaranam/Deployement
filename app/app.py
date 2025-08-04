from flask import Flask, render_template, request
from prometheus_client import Counter, Gauge
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # This exposes /metrics automatically

# Sample income entries
income_entries = [
    {"source": "Job", "amount": 50000},
    {"source": "Freelance", "amount": 15000}
]

# Prometheus custom metrics
income_add_counter = Counter('income_add_requests', 'Number of income add requests')
total_income_gauge = Gauge('total_income_amount', 'Total income amount')

@app.route('/')
def index():
    total = sum(entry['amount'] for entry in income_entries)
    total_income_gauge.set(total)
    return render_template("index.html", income=income_entries, total=total)

@app.route('/add', methods=['POST'])
def add_income():
    source = request.form['source']
    amount = float(request.form['amount'])
    income_entries.append({"source": source, "amount": amount})
    income_add_counter.inc()
    return index()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
