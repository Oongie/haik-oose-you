import os

from flask import Flask, redirect, render_template, request, url_for


def create_app(test_config=None):
    "Application factory function, returns the web app"
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite")
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/", methods=("GET", "POST"))
    def home():
        if request.method == "POST":
            return redirect(url_for("result"))

        return render_template("home.html")

    @app.route("/result", methods=("GET", "POST"))
    def result():
        # print(request.form["poem"])
        return render_template("result.html")

    return app

 