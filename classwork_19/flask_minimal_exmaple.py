import json

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Python Fundamentals'


@app.route('/start')
def start():
    return json.dumps({'username': 'marius', 'password': '<PASSWORD>'})


app.run()
