from re import M
import pytest
from app import app
from flask_mysqldbMySQL import MySQL


@pytest.fixture(scope="module")
def test_client():

    app.testing = True

    # Create a test client using the app config for testing
    with app.test_client() as test_client:

        yield test_client


@pytest.fixture(scope="function")
def create_test_database_connection():
    
    app.config.from_object("config.TestingConfig.test_database")

    with app.app_context():
        test_db = MySQL(app)
    
    yield test_db
        
