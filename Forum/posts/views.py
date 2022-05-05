from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Post
from django.contrib.auth.models import User

def index(request):
    posts = Post.objects.order_by('-date_posted')
    
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    paged_posts = paginator.get_page(page_number)
    
    
    context = {
        'posts':paged_posts
    }
    
    
    return render(request, 'posts/post-list.html', context)
    
def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    context = {
        'post': post
    }
    
    return render(request, 'posts/post.html', context)
    
def search(request):
    queryset_list = Post.objects.order_by('-date_posted')
    
    #Keyword
    if 'query' in request.GET:
        query = request.GET['query']
        if query:
            queryset_list = queryset_list.filter(content__icontains=query)
    
    #Author
    if 'author' in request.GET:
        author = request.GET['author']
        if author:
            queryset_list = queryset_list.filter(user__username__iexact=author)
    
    context = {
        'posts':queryset_list,
        'values': request.GET
    }
    
    return render(request, 'posts/search.html', context)


def newpost(request):
    return redirect('post/1')