#!/usr/bin/python3
"""
This Module is used to serve a web app on host = 0.0.0.0 and port = 5000
     it serves the root and hbnb child link
"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """This is the main entery of the host"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """A child entery to print HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=True)
def text(text):
    """This method recieves variable and appends to the return value"""
    text = str(escape(text))
    if text is not None:
        string = text.split('_')
        return "C {}".format(" ".join(string))


@app.route("/python/", strict_slashes=True)
@app.route("/python/<text>", strict_slashes=True)
def pythontext(text='is cool'):
    """This method returns the default value if no text is passed as
            argument to it, if not returns the value"""
    text = str(escape(text))
    if text is not None:
        string = text.split('_')
        return "Python {}".format(" ".join(string))


@app.route("/number/<int:n>", strict_slashes=True)
def number(n):
    """This method returns/displays 'n' is a number if it is integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    """This script runs if it is not imported"""
    app.run(debug=True, host='0.0.0.0', port=5000)
