#!/usr/bin/python3
"""
This Module is used to serve a web app on host = 0.0.0.0 and port = 5000
     it serves the root and hbnb child link
"""
from models import storage
from models.state import State
from flask import Flask
from flask import render_template
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


@app.route("/number_template/<int:n>", strict_slashes=True)
def numberTempl(n):
    """This method accepts an integers renders using render_template then
        returns the template which includes the number"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=True)
def oddOrEven(n):
    """This method accepts an integers renders using render_template then
        returns the template which includes the number and even/odd"""
    if isinstance(n, int):
        return render_template("6-number_odd_or_even.html", n=n)


@app.route('/states_list', strict_slashes=False)
def lists():
    """used to render and display the states list"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(error):
    """used to close the database after using it"""
    storage.close()


if __name__ == "__main__":
    """This script runs if it is not imported"""
    app.run(debug=True, host='0.0.0.0', port=5000)
