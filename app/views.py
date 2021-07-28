import os
import string
import random
import spotipy

from app import app

from flask import render_template, request, flash

from datetime import date, timedelta
from spotipy.oauth2 import SpotifyOAuth
from validate_email import validate_email

# Dictionary containing all my details
my_info = {
    "name": "Marcus Parker",
    "age": (date.today() - date(1993, 1, 8)) // timedelta(days=365.2425),
    "profession": "Software Engineer"
}


# Generate random string
def random_str_generator(size=15, chars=string.ascii_letters + string.digits):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))


# Authenticate spotify account
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["SPOTIPY_CLIENT_ID"],
                                               client_secret=os.environ["SPOTIPY_CLIENT_SECRET"],
                                               redirect_uri=os.environ["SPOTIPY_REDIRECT_URI"],
                                               state=random_str_generator(),
                                               scope="user-read-playback-position"),
                     requests_session=True
                     )

# List of routes
app_routes = [
    "/",
    "/portfolio",
    "/contact",
    "https://twitter.com/iDevelop_",
    "https://medium.com/@marcuseparker93",
    "https://www.linkedin.com/in/marcus-parker-124b6b211/",
]


@app.route("/")
def index():

    # Title of page
    title = "Homepage"

    # Create an empty list to store podcast images
    my_fave_podcast = []

    # Iterate over all currently saved episodes from my Spotify and add them to a list
    for episodes in range(len(sp.current_user_saved_episodes()) + 1):
        try:
            my_fave_podcast.append({
                "name": (sp.current_user_saved_episodes()["items"][episodes]["episode"]["show"]["name"]),
                "image": (sp.current_user_saved_episodes()["items"][episodes]["episode"]["images"][1]["url"]),
                "link": (sp.current_user_saved_episodes()["items"][episodes]["episode"]["show"]["external_urls"]["spotify"])
            })
        except IndexError as e:
            print(f"{e}")

    return render_template("public/index.html", title=title, podcast=my_fave_podcast, random_link=random.choice(app_routes))


@app.route("/portfolio")
def portfolio():

    # Title of page
    title = "Portfolio"

    return render_template("public/portfolio.html", title=title, random_link=random.choice(app_routes))


@app.route("/contact", methods=["GET", "POST"])
def contact():

    # Title of page
    title = "Contact"

    # User reached route via POST method
    if request.method == "POST":

        # Collect data from form
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        # Check if the email is valid
        is_valid = validate_email(email)

        # Ensure all information is submitted
        if not request.form["name"]:
            flash("Please enter a name", category="error")

        elif not request.form["subject"]:
            flash("Please enter a subject", category="error")

        elif not request.form["message"]:
            flash("Please include a message", category="error")

        if not request.form["email"]:
            flash("Please enter an email", category="error")

        elif not is_valid:
            flash("Please enter a valid email address", category="error")

        return render_template("public/submit.html", title=title, random_link=random.choice(app_routes))

    # User reached route via GET method
    else:
        return render_template("public/contact.html", title=title, random_link=random.choice(app_routes))