import secrets

from flask import Flask, flash, redirect, render_template, url_for
from forms import WebinarForm

app = Flask(__name__)
secrets.token_urlsafe(64)


@app.route("/")
def index():
    """
    Home page
    :return:
    """
    return render_template("index.html")


@app.route("/webinar", methods=["GET", "POST"])
def webinar():
    """
    Form page
    :return:
    """
    form = WebinarForm()

    if form.validate_on_submit():
        flash("Thanks for filling out the form!")
        redirect(url_for("index"))

    return render_template("webinar.html")
