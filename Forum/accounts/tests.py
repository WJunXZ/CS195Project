from django.test import TestCase
import unittest
from django.test import Client
# Create your tests here.


class AccountsLoginTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/accounts/login')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

class AccountsDashboardTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/accounts/dashboard')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

class AccountsRegisterTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/accounts/register')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

