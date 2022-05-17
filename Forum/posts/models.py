from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateField(default=datetime.now)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title