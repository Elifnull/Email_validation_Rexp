from crypt import methods
from flask_app import app
from flask_app.models.email import Email
from flask import flash, render_template, request, redirect

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_email", methods=["POST"])
def email_create():
    if not Email.validate_email(request.form):
        return redirect("/")
    Email.save(request.form)
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    return render_template("results.html", emails = Email.get_all())
