from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    loan_amount = float(request.form['loan_amount'])
    interest_rate = float(request.form['interest_rate']) / 100
    loan_term = int(request.form['loan_term'])

    monthly_interest_rate = interest_rate / 12
    total_payments = loan_term * 12

    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (-total_payments))
    total_cost = monthly_payment * total_payments
    total_interest = total_cost - loan_amount

    return render_template('result.html', monthly_payment=monthly_payment, total_cost=total_cost,
                           total_interest=total_interest)


if __name__ == '__main__':
    app.run(debug=True)
