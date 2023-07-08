from flask import Flask, render_template, request, flash
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secr3t'
# Function to fetch exchange rate data from the API
def fetch_exchange_rates():
    url = "https://api.exchangerate.host/latest"
    response = requests.get(url)
    data = response.json()
    return data


# Home route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Fetch exchange rate data
        exchange_data = fetch_exchange_rates()
        base_currency = exchange_data['base']
        date = exchange_data['date']
        rates = exchange_data['rates']

        # Get form data
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        flash("Valid entry")

        # Convert currencies
        converted_amount = amount * rates[to_currency] / rates[from_currency]
        
        
        return render_template('form.html', base_currency=base_currency, date=date, rates=rates,
                               converted_amount=converted_amount, from_currency=from_currency,
                               to_currency=to_currency, amount=amount)

   

    # Fetch exchange rate data
    exchange_data = fetch_exchange_rates()
    rates = exchange_data['rates']

    
    return render_template('form.html', rates=rates)


if __name__ == '__main__':
    app.run(debug=True)