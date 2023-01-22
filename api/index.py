from flask import Flask
# import function good_morning from routes>test.py
from routes import *

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'


@app.route('/good_morning')
good_morning()