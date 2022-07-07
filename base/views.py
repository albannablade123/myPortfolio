from django.shortcuts import render
from django.http import HttpResponse


from .models import Post
# Create your views here.

def home(request):
    return render(request,'base/index.html')

def posts(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'base/posts.html', context)

def post(request):
    return render(request,'base/post.html')

def profile(request):
    return render(request,'base/profile.html')