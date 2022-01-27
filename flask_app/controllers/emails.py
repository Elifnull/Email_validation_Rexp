from flask_app import app
from flask import flash, render_template

@app.route("/")
def index():
    return render_template("index.html")

