from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30, help_text="First name of the user")
    last_name = models.CharField(max_length=30, help_text="Last name of the user")
    email = models.EmailField(help_text="User email")

    def __str__(self):
        return self.content


class Post(models.Model):
    title = models.CharField(max_length=100, help_text="The title of the post created by the user")
    content = models.CharField(max_length=1000, help_text="The content of the post created by the user")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(verbose_name="Date")

    def __str__(self):
        return self.content

class Comment(models.Model):
    content = models.CharField(max_length=500, help_text="Comment made in response to another post")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(verbose_name="Date")
    post_commented_on = models.ForeignKey(Post, help_text="The post this comment was in response to", on_delete=models.CASCADE)

    def __str__(self):
        return self.content




