#!/usr/bin/python3
"""This script starts a Flask web application with multiple routes"""

from flask import Flask
from flask import render_template


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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_fun(text):
    """The route for python text"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """The route for number"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """The route for number template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """The route for number odd or even"""
    call = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, call=call)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
