from django.urls import path
from . import views

urlpatterns = [
    path('newcomment', views.new_comment, name='newcomment'),
]
