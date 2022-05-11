from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . models import Comment
from posts.models import Post
from django.http import HttpResponse
# Create your views here.

def new_comment(request):
    if request.method=="POST":
        title = request.POST['title']
        content = request.POST['commentcontent']
        original_post = request.POST['post_id']
        original_post = Post.objects.get(pk=original_post)
        
        comment = Comment(user=request.user, original_post=original_post, title=title, content=content)
        comment.save()
        
        
        url = '/post/' + str(original_post.pk)
        return HttpResponseRedirect(url)
    else:
        print("I'm here")
        return HttpResponseRedirect('')