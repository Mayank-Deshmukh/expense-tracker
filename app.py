from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    Amount = request.form['Amount']
    Category = request.form['Category']
    Description = request.form['Description']
    Gateway = request.form['Gateway']
    Date = request.form['expense-date']

    try:
        expense_data = pd.read_excel('expense_data.xlsx')
    except FileNotFoundError:
        expense_data = pd.DataFrame(columns=['Amount', 'Category', 'Description', 'Gateway', 'Date'])
    
    new_entry = pd.DataFrame({'Amount': [Amount], 'Category': [Category], 'Description': [Description], 'Gateway': [Gateway], 'Date': [Date]})
    expense_data = pd.concat([expense_data, new_entry], ignore_index=True)
    expense_data.to_excel('expense_data.xlsx', index=False)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
