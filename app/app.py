from flask import Flask, render_template, request
from prometheus_client import Counter, generate_latest, Gauge

app = Flask(__name__)

# Sample income entries
income_entries = [
    {"source": "Job", "amount": 50000},
    {"source": "Freelance", "amount": 15000}
]

# PROMETHEUS METRICS
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

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
