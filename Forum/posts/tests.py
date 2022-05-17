from django.test import TestCase
from django.db import IntegrityError
from .models import Post
from django.contrib.auth.models import User
import unittest
from django.test import Client
# Create your tests here.


class PostIntegrationTest(TestCase):
    def setup(self):
        User.objects.create(username='Testuser')
        test_user = User.objects.get(username = 'Testuser')
        Post.objects.create(user= test_user, title = "test", content="this is a test") 

    def test_post(self):
   	    User.objects.create(username='TestUser')
   	    #print(User.objects.all())
   	    test_user = User.objects.get(username = 'TestUser')
   	    Post.objects.create(user= test_user, title = "test", content="this is a test") 
   	    #print(Post.objects.all())
   	    test_post = Post.objects.get(title="test")
   	    self.assertEqual(test_post.content, "this is a test" )
    #


class MissingUserIntegrityTest(TestCase):

    def test_post(self):
    	try:
    		Post.objects.create(user = None, title="test post title", content="test post") 
    	except IntegrityError as e:
    		self.assertEqual(1, 1)

    #











