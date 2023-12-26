#!/usr/bin/python3
"""
This Module is used to serve a web app on host = 0.0.0.0 and port = 5000
     it serves at the root only
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """This is the main entery of the host"""
    return "Hello HBNB"


if __name__ == "__main__":
    """This script runs if it is not imported"""
    app.run(host='0.0.0.0', port=5000)
