from django.test import TestCase
from django.db import IntegrityError
from .models import Comment
from posts.models import Post
from django.contrib.auth.models import User
import unittest
from django.test import Client
# Create your tests here.


class CommentIntegrationTest(TestCase):

    def test_post(self):
   	    User.objects.create(username='TestUser')
   	    #print(User.objects.all())
   	    test_user = User.objects.get(username = 'TestUser')
   	    Post.objects.create(user= test_user, title = "test", content="this is a test") 
   	    #print(Post.objects.all())
   	    test_post = Post.objects.get(title="test")
   	    self.assertEqual(test_post.content, "this is a test" )
   	    Comment.objects.create(user = test_user, original_post= test_post, title="test comment title", content="test comment")
   	    test_comment = Comment.objects.get(title="test comment title")
   	    self.assertEqual(test_comment.content, "test comment")
    #

class CommentTestCaseNoUserOrPost(TestCase):

    def test_post(self):
    	try:
    		Comment.objects.create(user = None, original_post= None, title="test comment title", content="test comment") 
    	except IntegrityError as e:
    		self.assertEqual(1, 1)

    #



