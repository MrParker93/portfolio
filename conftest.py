import pytest
from app import app
from flask_mysqldb import MySQL

@pytest.fixture(scope="module")
def test_client():

    app.testing = True

    # Create a test client using the app config for testing
    with app.test_client() as test_client:

        yield test_client

@pytest.fixture(scope="function")
def create_database_connection():

    with app.app_context():
        
        test_db = MySQL(app)
        yield test_db.connect
        
