#!/usr/bin/python3
"""
    odd or even
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """
        Hello_HBNB function
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """
        HBNB function
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """
        /c/<text> function
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """
        /python/<text> function
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
        /number/<int:n> function
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
        /number_template/<int:n> function
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
        /number_odd_or_even/<int:n> function
    """
    if n % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    return render_template('6-number_odd_or_even.html',
                           n=n, even_or_odd=even_or_odd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
