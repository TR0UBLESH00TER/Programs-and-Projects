from flask import Flask, render_template, request
from datetime import datetime
import requests
import os

def qotd():
    year = datetime.now().year
    url = "https://quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com/quote"

    querystring = {"token":"ipworld.info"}

    headers = {
            'x-rapidapi-key': os.getenv('x-rapidapi-key'),
            'x-rapidapi-host': "quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = eval(response.text)
    return data["text"],data["author"]

app = Flask(__name__)

@app.route('/')
def index():
    year = datetime.now().year
    quote,author=qotd()
    return render_template('index.html',year=year,quote=quote,author=author)

@app.route('/home')
def home():
    year = datetime.now().year
    quote,author=qotd()
    return render_template('index.html',year=year,quote=quote,author=author)

@app.route('/buttons')
def buttons():
    year = datetime.now().year
    return render_template('buttons.html',year=year)

@app.route('/about')
def about():
    year = datetime.now().year
    return render_template('about.html',year=year)

app.run(host='0.0.0.0', port=8080)