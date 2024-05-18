#!/usr/bin/python3
"""This script start a flask application with two routes"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """The first route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """The route for hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """The route for c text"""
    return "C " + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
