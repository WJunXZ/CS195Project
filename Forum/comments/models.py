from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from posts.models import Post

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    original_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.title