from unittest import mock, TestCase
import mysql.connector
import requests
import json

from Controller import DatabaseController
db = DatabaseController.DatabaseControl()

DB = ""
HOST = "localhost"
USER = "root"
PASSWORD = ""
PORT = 3306


class TestDatabase(TestCase):
    def test_list_orders_works(self):
        self.assertEqual(200, db.list_orders().code)
        

    