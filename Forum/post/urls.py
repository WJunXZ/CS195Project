from django.contrib import auth
from django.urls import path
from . import views


urlpatterns = [path('', views.welcome_view, name="home_screen"),
path('posts/', views.posts_page, name="posts_page"),
path('posts/<int:pk>/', views.post_details, name="post_details")]