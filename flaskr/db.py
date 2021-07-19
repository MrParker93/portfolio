import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


# Create a connection to a database
def get_db():

    # g is a namespace object, unique to each request. It stores data that might be accessed by multiple functions
    # during a single request. g stores the connection and reuses it every time get_db is called for optimal processing
    if "db" not in g:
        g.db = sqlite3.connect(
            # Similar to g, current_app points to the Flask app handling the request
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # Return database rows as dicts
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    # Opens file relative to the directory
    with current_app.open_resource("schema.sql") as file:
        db.executescript(file.read().decode("utf8"))


# Command function defines a CLI command called init-db with_appcontext ensures the command inside the function is ran
# With the command
@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()

    # Prints a message to the terminal
    click.echo("Initialised the database.")


# Add the registration to the application instance
def init_app(app):

    # Call close_db after returning the response
    app.teardown_appcontext(close_db)

    # Adds init_db_command as command that can be called with flask (eg "flask init_db_command")
    app.cli.add_command(init_db_command)
