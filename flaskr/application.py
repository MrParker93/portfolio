from flask import Blueprint, render_template, request, redirect, flash
from datetime import date, timedelta

# Configure app
bp = Blueprint("main", __name__)

# Dictionary containing all my details
my_info = {
    "name": "Marcus Parker",
    "age": (date.today() - date(1993, 1, 8)) // timedelta(days=365.2425),
    "profession": "Software Engineer"
}


@bp.route("/")
def index():

    # Title of page
    title = "Homepage"
    return render_template("index.html", name=my_info["name"], profession=my_info["profession"], title=title)


@bp.route("/portfolio")
def portfolio():

    # Title of page
    title = "Portfolio"
    return render_template("portfolio.html", name=my_info["name"], profession=my_info["profession"], title=title)


@bp.route("/contact")
def contact():

    # Title of page
    title = "Contact"
    return render_template("contact.html", name=my_info["name"], profession=my_info["profession"], title=title)
