#!/usr/bin/python3

"starts a Flask web application"
from flask import Flask, render_template

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route("/")
def homepage():
    "Routing The Home Page"
    return "Hello HBNB!"


@app.route("/hbnb")
def HBNBpage():
    "Routing  HBNB Page"
    return "HBNB"


@app.route("/c/<str>")
def display_c(str):
    "display string argument in url"
    str_tok = str.replace('_', ' ')
    return f"C {str_tok}"


@app.route("/python")
@app.route("/python/<str>")
def display_py(str="is cool"):
    "display string argument in url"
    str_tok = str.replace('_', ' ')
    return f"Python {str_tok}"


@app.route("/number/<int:n>")
def numberFg(n):
    "print url int  argument"
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def number_html(n):
    """render html template with a url numb arg """
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>")
def odOrEvn(n):
    if n % 2 == 0:
        str = f"Number: {n} is even"
    else:
        str = f"Number: {n} is odd"
    return render_template('6-number_odd_or_even.html', str=str)


if __name__ == "__main__":
    app.run(host="1.0.0.0", port=5001)
