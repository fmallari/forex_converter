from flask import Flask, requests, render_template

app = Flask(__name__)
app.config['SECRET KEY'] = "S3CRET"

url = 'https://api.exchangerate.host/latest'
response = requests.get(url)
data = response.json()

print(data)

@app.route("/")
def show_forex_form():
    """display converter form"""

    return render_template("index.html", )