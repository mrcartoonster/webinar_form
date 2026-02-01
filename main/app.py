import secrets

from flask import Flask, flash, redirect, render_template, url_for
from forms import WebinarForm

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(64)


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
        return redirect(url_for("index"))

    #   elif request.method == 'POST':
    #       flash("The form didn't record your name. Please try again.")
    #       return redirect(url_for("webinar"))

    return render_template("webinar.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
