from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-date_posted').filter(featured=True)[:3]
    
    context = {
        'posts':posts
    }
    
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
