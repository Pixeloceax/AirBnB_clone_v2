#!/usr/bin/python3
from flask import Flask
"""
    Hello
"""

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
