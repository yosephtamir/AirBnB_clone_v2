#!/usr/bin/python3
"""
This Module is used to serve a web app on host = 0.0.0.0 and port = 5000
     it serves the root and hbnb child link
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """This is the main entery of the host"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """A child entery to print HBNB"""
    return "HBNB"


if __name__ == "__main__":
    """This script runs if it is not imported"""
    app.run(host='0.0.0.0', port=5000)
