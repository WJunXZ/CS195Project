from django.shortcuts import get_object_or_404, render
from .models import Post, User, Comment

# Create your views here.
def welcome_view(request):
    return render(request, 'base.html')

def posts_page(request):
    posts = Post.objects.all()
    post_list = []

    for post in posts:
        post_list.append({'post':post})
        

    context = {'post_list': post_list}

    return render(request, 'post/post_page.html', context)

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment_set.all()

    if comments:

        context = {
            'post': post,
            'comment' : comments
        }
    else:
        context = {
            'post': post,
            'comment': None
        }

    return render(request, 'post/post_details.html', context)
