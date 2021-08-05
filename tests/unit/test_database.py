import os
import pytest
from app import app


class TestCase:

    def test_database_is_connected(self, create_database_connection):
        test_db = create_database_connection
        test_db.begin()
        cursor = test_db.cursor()
        exists = cursor._get_db()
        assert exists != None

    def test_database_deletes_and_creates_databases(self, create_database_connection):
        test_db = create_database_connection
        test_db.begin()
        cursor = test_db.cursor()
        cursor.execute("DROP DATABASE IF EXISTS {}".format(
            app.config["MYSQL_DB"]))
        cursor.execute("CREATE DATABASE {}".format(app.config["MYSQL_DB"]))
        cursor.execute("SHOW DATABASES LIKE '{}'".format(
            app.config["MYSQL_DB"]))
        result = cursor.fetchall()
        assert len(result) == 1

    def test_database_deletes_and_creates_tables(self, create_database_connection):
        test_db = create_database_connection
        test_db.begin()
        cursor = test_db.cursor()
        cursor.execute("DROP TABLE IF EXISTS email")
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS email (
            `id` INT NOT NULL AUTO_INCREMENT,
            `name` TEXT NOT NULL, 
            `email` VARCHAR(255) NOT NULL,
            `subject` TEXT NOT NULL,
            `message` TEXT NOT NULL,
            `datetime` DATETIME on update CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`id`))
            """
        )
        cursor.execute("SHOW TABLES LIKE 'email'")
        result = cursor.fetchall()
        assert len(result) == 1

    @pytest.mark.parametrize("name, email, subject, message", [
        ("foo", "foo@foo.com", "foo", "foo"),
        ("bar", "bar@bar.com", "bar", "bar"),
        ("baz", "baz@baz.com", "baz", "baz"),
        ("test", "test@test.com", "test", "test")
    ])
    def test_database_inserts_and_deletes_data(self, create_database_connection, name, email, subject, message):
        test_db = create_database_connection
        test_db.begin()
        cursor = test_db.cursor()
        cursor.execute("INSERT INTO email (name, email, subject, message) VALUES (%s, %s, %s, %s)",
                       (name, email, subject, message))
        result = cursor.rowcount
        assert result == 1
