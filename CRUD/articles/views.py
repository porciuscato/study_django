from django.shortcuts import render, redirect
from articles import views
from .models import Articles

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    article = Articles()
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    article.img_url = request.GET.get('img_url')
    article.save()
    return redirect('index')

def index(request):
    articles = reversed(Articles.objects.all())
    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)