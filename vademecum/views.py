from django.shortcuts import render, redirect
from .models import Post
from .forms import RegisterForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts})

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "register.html", {"form":form})