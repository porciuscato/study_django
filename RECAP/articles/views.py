from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from IPython import embed
from django.http import Http404
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

# detail
def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    # article = get_object_or_404(Article, pk=pk)
    # 만약 article.objects.get(pk=pk) 여기서 에러가 나면 에러를 침
    try:
        # 에러가 날 만한 코드를 넣자
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        raise Http404('해당하는 ID의 글이 존재하지 않습니다.')
    
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)


# # create
# def create(request):
#     # get과 post로 나눠서 만들어보자
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         Article.objects.create(title=title, content=content)
#         return redirect('articles:index')
#     else:
#         return render(request, 'articles/create.html')

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        embed()
        # 전송된 데이터가 유효한 값인지 검사
        if form.is_valid():
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title,content=content)
            article = form.save()
        # 사실 위 처럼 적을 필요 없이
        # form.save()
        # 하면 자동으로 저장됨
            return redirect(article)
        else:
            return redirect('articles:create')



###############################################
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # new_article = Article.objects.create(
        #         title=title,
        #         content=content,
        #     )
###############################################
        # print(new_article.pk)
        # detail 페이지로 보냄
        # return redirect('articles:detail', new_article.pk)
        
        # 혹은 이렇게도 작성할 수 있음

        # return redirect(new_article)
        # redirect 에 객체만 전달했는데도 detail 페이지를 띠우더라
        # 객체 안에 absoulute_url이 있는지 확인한 뒤 redirct를 해준다
        # 객체가 들어오면 해당하는 객체가 있는지 없는지 판단하는 것이 있음

    else:
        form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html', context)


# update -> articles/:id/update | (PUT) articles/:id
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # 실제 DB의 데이터를 수정
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            form.save()
            return redirect(article)
        else:
            form = ArticleForm(
            initial={
                'title': article.title,
                'content': article.content,
            })
            return redirect(article)
    # 편집화면
    
    # form = ArticleForm(
    #     initial={
    #         'title': article.title,
    #         'content': article.content,
    # })
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


# delete -> article/:id/delete
# POST일 때만 반응하도록 만드는 것
@require_POST
def delete(request, pk):
    # POST로 요청이 올 때만, 지우는 걸로
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect(article)
