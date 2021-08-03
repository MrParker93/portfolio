import pytest
from app import app
from flask import current_app


@pytest.fixture(scope="module")
def test_client():

    # Create a test client using the app config for testing
    with app.test_client() as test_client:

        with app.app_context():
            current_app.config["ENV"] = "testing"
            yield test_client