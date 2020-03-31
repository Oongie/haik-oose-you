# A small app following the user guide
from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/hello")
def hello_world():
    return "Hello!"

@app.route("/user/<username>")
def show_uer_profile(username):
    return "User %s" % escape(username)
