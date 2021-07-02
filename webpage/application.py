import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask_mail import Message, Mail
from .forms import ContactForm
from webpage.db import get_db


bp = Blueprint("application", __name__)
mail = Mail()


@bp.route("/")
def index():
    # Display homepage
    return render_template("index.html")


@bp.route("/about")
def about():
    # Display about page
    return render_template("about.html")


@bp.route("/portfolio")
def portfolio():
    # Display portfolio page
    return render_template("portfolio.html")


@bp.route("/blog")
def blog():
    # Display blog posts from medium
    return render_template("blog.html")


@bp.route("/achievements")
def achievements():
    # Display achievements page
    return render_template("achievements.html")


@bp.route("/contact", methods=["GET", "POST"])
def contact():
    # Display contact form
    form = ContactForm()

    # User reached route via POST (as by submitting a form etc)
    if request.method == "POST":
        # Ensure all fields are submitted
        if not form.validate():
            flash("All fields are required.", category="error")
            return render_template("contact.html", form=form)
        else:
            msg = Message(form.subject.data, sender="marcuseparker93@gmail.com",
                          recipients=["marcuseparker@hotmail.com"])
            msg.body = """
            %s
            From %s <%s>
            """ % (form.message.data, form.name.data, form.email.data)
            mail.send(msg)

            return render_template("contact.html", success=True)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("contact.html", form=form)
