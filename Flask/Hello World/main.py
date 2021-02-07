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
    footer = f'Built with ♥ using <strong>Flask</strong> and <strong>Bulma</strong><br />&copy; {year} TR0UBLESH00TER '
    return render_template('index.html',footer=footer,quote=quote,author=author)

@app.route('/home')
def home():
    year = datetime.now().year
    quote,author=qotd()
    footer = f'Built with ♥ using <strong>Flask</strong> and <strong>Bulma</strong><br />&copy; {year} TR0UBLESH00TER '
    return render_template('index.html',footer=footer,quote=quote,author=author)

@app.route('/buttons')
def buttons():
    year = datetime.now().year
    footer = f'Built with ♥ using <strong>Flask</strong> and <strong>Bulma</strong><br />&copy; {year} TR0UBLESH00TER '
    return render_template('buttons.html',footer=footer)

@app.route('/about')
def about():
    year = datetime.now().year
    footer = f'Built with ♥ using <strong>Flask</strong> and <strong>Bulma</strong><br />&copy; {year} TR0UBLESH00TER '
    return render_template('about.html',footer=footer)