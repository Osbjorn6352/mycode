#!/usr/bin/python3
"""Test Suite for email_reg"""

import unittest
import sqlite3
from flask import Flask, redirect, url_for
from email_reg import get_db_connection, get_subscribers, app     # these are the functions we want to test and our instance of the Flask server class

class DatabaseConnectionTest(unittest.TestCase):                # creates a subclass from the TestCase class in the unittest library
    def test_get_db_connection(self):                           # creates a new instance method
        with app.app_context():                                 # creates a context for the Flask application
            conn = get_db_connection()                          # this is the function we are testing; conn should hold the connection
            self.assertIsInstance(conn, sqlite3.Connection)     # this checks to see if our connection is an instance of the sqlite3.Connection class
            conn.close()                                        # this closes the connection

class SubscriberManagementTest(unittest.TestCase):              # creates a subclass from the TestCase class in the unittest library
    @classmethod                                                # this defines the next method as a class method (rather than an instance method)
    def setUpClass(cls):                                        # this method sets up a context in which to run our test
        with app.app_context():
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS subscribers (email text)''')
            c.execute("DELETE FROM subscribers")
            c.execute("INSERT INTO subscribers VALUES ('test1@example.com')")
            conn.commit()
            c.close()
            conn.close()

    def setUp(self):                                            # this sets up a test_client to send HTTP requests within the test cases
        self.app = app.test_client()

    def test_get_subscribers(self):                             # this is the heart of the test; the previous is set up.
        with app.app_context():
            subscribers = get_subscribers()
        self.assertEqual(len(subscribers), 1)
        self.assertEqual(subscribers[0]['email'], 'test1@example.com')

if __name__ == '__main__':
    unittest.main()

