from IPython import embed
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm, CommentForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'article/index.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'article/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # ??
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            # context = {
            #     'aritcle': article,
            # }
            return redirect(article)
            
            
    else:
        form = ArticleForm()
        context = {
            'form' : form,
        }
        return render(request, 'article/create.html', context)
    