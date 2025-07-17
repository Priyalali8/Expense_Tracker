from flask import Flask, render_template, request, redirect
from main import get_message, add_expense, view_expenses

app = Flask(__name__)

@app.route('/')
def home():
    expenses = view_expenses()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add():
    description = request.form['description']
    amount = request.form['amount']
    date = request.form['date']
    add_expense(description, amount, date)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
