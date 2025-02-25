from flask import Flask, request
import requests
import sqlite3
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Forex Trading API!"

# Insecure API key storage (vulnerability for demo)
API_KEY = os.environ.get('FOREX_API_KEY', 'insecure_key_123')  # Hardcoded API key (vulnerable)

# Insecure SQL query (vulnerability for demo)
def get_user(email):
    conn = sqlite3.connect('traders.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM traders WHERE email = '{email}'"  # SQL injection risk
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result

@app.route('/rates/<currency>', methods=['GET'])
def get_rates(currency):
    url = f"https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=USD&to_symbol={currency}&apikey={API_KEY}"
    response = requests.get(url)
    return response.json()

@app.route('/trade', methods=['POST'])
def trade():
    email = request.form.get('email')
    user = get_user(email)
    if user:
        return f"Trade executed for {email}"
    return "User not found"

    @app.route('/rates/<currency>', methods=['GET'])
def get_rates(currency):
    url = f"https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=USD&to_symbol={currency}&apikey={API_KEY}"
    response = requests.get(url).json()
    rates = response.get("Time Series FX (Daily)", {})
    return jsonify(rates)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)