import datetime
import os

from flask import Flask, redirect, render_template, request, url_for, session

from app.db import get_db, init_app_db


def create_app(test_config=None):
    "Application factory function, returns the web app"
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "app.sqlite")
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
    
    # Initialise database
    init_app_db(app)

    @app.route("/", methods=("GET", "POST"))
    def home():
        db = get_db()

        if request.method == "POST":
            poem = request.form["poem"]
            db.execute("""INSERT INTO fact_poem (poem) VALUES (?)
            """, (poem,))
            db.commit()

            # Store the poem so the results template can access
            session["poem"] = poem 

            return redirect(url_for("result"))

        return render_template("home.html")

    @app.route("/result", methods=("GET", "POST"))
    def result():
        db = get_db()
        if request.method == "GET":
            poem = session.get("poem")
            if poem is None:
                poem = "Enter some text!"
            print(poem)

        elif request.method == "POST":
            poem = request.form["poem"]
            db.execute("""INSERT INTO fact_poem (poem) VALUES (?)
            """, (poem,))
            db.commit()

            # Store the poem so the results template can access
            session["poem"] = poem 

        return render_template("result.html")

    return app

 