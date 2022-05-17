from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Post
from comments.models import Comment
from django.contrib.auth.models import User

"""
Summary
Function Name: index
Description: Returns the post list page with all the posts, at 5 per page
"""

def index(request):
    posts = Post.objects.order_by('-id')
    
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    paged_posts = paginator.get_page(page_number)
    
    
    context = {
        'posts':paged_posts
    }
    
    
    return render(request, 'posts/post-list.html', context)

"""
Summary
Function Name: post
Description: Returns the post-detail page for a specific post
"""
    
def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(original_post=post_id)
    
    context = {
        'post': post,
        'comments': comments
    }
    
    return render(request, 'posts/post.html', context)


"""
Summary
Function Name: search
Description: Takes users search queries and returns posts macthing them
"""    
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

"""
Summary
Function Name: newpost
Description: Takes the info passed by a user and creates a new Post object in DB and then redirects to that post page
"""
def newpost(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['postcontent']
        
        post = Post(user = request.user, title=title, content = content)
        post.save()
        
        url = '' + str(post.pk)
        return HttpResponseRedirect(url)