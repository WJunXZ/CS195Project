from django.shortcuts import render

# Create your views here.
def postPage(request):
    id = request.GET.get('post_id')
    return render(request, 'base.html', {"post_id": id})

def index(request):
    return render(request, 'index.html')