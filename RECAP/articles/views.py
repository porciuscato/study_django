from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

# detail
def detail(request, pk):
    article = Article.objects.get(pk=pk)
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
        # 전송된 데이터가 유효한 값인지 검사
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article.objects.create(title=title,content=content)
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