from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

import requests 

app = Flask(__name__)
app.config['SECRET_KEY'] = "S3CRET"

debug = DebugToolbarExtension(app)

url = 'https://api.exchangerate.host/latest'
response = requests.get(url)
data = response.json()

print(data)

@app.route("/")
def homepage_form():
    """display converter form"""

    return render_template("form.html")

@app.route("/result", methods=["POST"])
def convert_currency():
    """Convert currency after selecting Convert button"""
    currency1 = request.args("from")
    print(currency1);
    currency2 = request.args("to")
    print(currency2);
    amount = request.args.get("amount")
    print(amount)

    return render_template("form.html")