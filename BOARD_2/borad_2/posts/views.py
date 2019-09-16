from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'posts/index.html', context)

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('text')
        Post.objects.create(title=title,content=content)
        return redirect('posts:index')
    else:
        return render(request, 'posts/create.html')

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'posts/detail.html', context)

def update(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    if request.method == 'POST':

        return redirect('posts:index')
    else:
        context = {
            'post': post,
        }
        return render(request, 'posts/update.html', context)

def delete(request, pk):
    return redirect(request, 'posts:index')