from django.test import TestCase
import unittest
from django.test import Client
from posts.models import Post
from django.contrib.auth.models import User
# Create your tests here.


class PostViewTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/post/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

""" class AboutViewTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/about')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200) """

class PostThreadViewTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        
    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/post/', {'pk':1})

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)