from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from posts.models import Post

# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
                    #Login Immediately
                    auth.login(request, user)
                    messages.success(request, "Account Created, Succesfully Logged in ")
                    return redirect('index')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Succesfully Logged In")
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def dashboard(request):
    username = 'guest'
    posts = None
    if request.user.is_authenticated:
        username = request.user.get_short_name
        posts = Post.objects.filter(user=request.user)
    
    context = {
        'name': username,
        'posts': posts
    }
    
    return render(request, 'accounts/dashboard.html', context)

def logout(request):
    return redirect('index')