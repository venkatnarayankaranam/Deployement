from flask import Flask, render_template, request

app = Flask(__name__)

# Sample income entries
income_entries = [
    {"source": "Job", "amount": 50000},
    {"source": "Freelance", "amount": 15000}
]

@app.route('/')
def index():
    total = sum(entry['amount'] for entry in income_entries)
    return render_template("index.html", income=income_entries, total=total)

@app.route('/add', methods=['POST'])
def add_income():
    source = request.form['source']
    amount = float(request.form['amount'])
    income_entries.append({"source": source, "amount": amount})
    return index()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
