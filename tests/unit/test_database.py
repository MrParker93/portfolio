import os
import pytest
from flask_mysqldb import MySQL


def test_database_creates_tables(test_client, create_test_database_connection):
    """
    GIVEN a test database
    WHEN a table is created
    THEN check for creation of that table
    """
        

    cursor = test_db.connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS test")

    test_db.commit

    res = cursor._get_db

    cursor.close()

    assert res == cursor._get_db
