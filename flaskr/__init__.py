import os
from flask import Flask


def create_app(test_config=None):

    # Create and configure Flask app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "db.sqlite"),
    )

    if test_config is None:

        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)  # TODO: CHANGE SECRET_KEY TO A LONG RANDOM VALUE WHEN DEPLOYING
    else:

        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register the function to the app
    from . import db
    db.init_app(app)

    # Register the blueprint with the app
    from . import application
    app.register_blueprint(application.bp)

    return app
