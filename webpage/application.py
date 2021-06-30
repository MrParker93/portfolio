import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from webpage.db import get_db

bp = Blueprint("application", __name__)


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

@bp.route("/contact")
def contact():
    # Display contact form
    return render_template("contact.html")