from flask import Flask, render_template, request, flash
import requests

app = Flask(__name__)


url = 'https://api.exchangerate.host/latest'
response = requests.get(url)
data = response.json()

print(data)

    return render_template('form.html', rates=rates)


if __name__ == '__main__':
    app.run(debug=True)

    return render_template("form.html")