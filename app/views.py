import os
import pprint
import string
import random
import spotipy

from app import app
from functions import random_str_generator, send_message

from flask import render_template, request, flash, redirect
from flask_mail import Mail
from flask_mysqldb import MySQL

from datetime import date, timedelta
from spotipy.oauth2 import SpotifyOAuth
from validate_email import validate_email

# Dictionary containing all my details
my_info = {
    "name": "Marcus Parker",
    "age": (date.today() - date(1993, 1, 8)) // timedelta(days=365.2425),
    "profession": "Software Engineer"
}

# Authenticate spotify account
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["SPOTIPY_CLIENT_ID"],
                                               client_secret=os.environ["SPOTIPY_CLIENT_SECRET"],
                                               redirect_uri=os.environ["SPOTIPY_REDIRECT_URI"],
                                               state=random_str_generator(),
                                               scope="user-read-playback-position"),
                     requests_session=True
                     )


# Create mail object
mail = Mail(app)

# Create MYSQL object
mysql = MySQL(app)

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

    return render_template("public/portfolio.html", title=title, name=my_info["name"], random_link=random.choice(app_routes))


@app.route("/contact", methods=["GET", "POST"])
def contact():

    # Title of page
    title = "Contact"

    # User reached route via POST method
    if request.method == "POST":

        req = request.form

        # Collect data from form
        name = req["name"]
        email = req["email"]
        subject = req["subject"]
        message = req["message"]

        # Check if the email is valid
        is_valid = validate_email(email)

        # Ensure all information is submitted
        if not req["name"]:
            flash("Please enter a name", "danger")
            return redirect(request.url)

        if not req["email"]:
            flash("Please enter an email", "danger")
            return redirect(request.url)

        if not is_valid:
            flash("Please enter a valid email address", "danger")
            return redirect(request.url)

        if not req["subject"]:
            flash("Please enter a subject", "danger")
            return redirect(request.url)

        if not req["message"]:
            flash("Please include a message", "danger")
            return redirect(request.url)

        
         # Send the email to my email address
        send_message(req, mail)

        # Create a cursor to traverse the database
        cursor = mysql.connection.cursor()

        # Store MySQL query in a variable
        add_message_to_database = "INSERT INTO email (name, email, subject, message) VALUES (%s, %s, %s, %s)"

        # Store all form data in a variable
        form_info = (name, email, subject, message)

        # Insert form information into database
        cursor.execute(add_message_to_database, form_info)

         # Commit the changes to the database and close the connection
        mysql.connection.commit()
        cursor.close()

        return render_template("public/submit.html", title=title, random_link=random.choice(app_routes))

    # User reached route via GET method
    else:
        return render_template("public/contact.html", title=title, random_link=random.choice(app_routes))
