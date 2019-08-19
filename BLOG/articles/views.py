from django.shortcuts import render, redirect
from datetime import datetime
# DB에서 가져오기 위한 import 방법
from .models import Article

blogs = [
    # ('제목','내용'),
]

# class Article:
#     def __init__(self, title, content, created_at):
#         self.title = title
#         self.content = content
#         self.created_at = created_at

#     def __str__(self):
#         return '제목: {} 내용: {} 시간: {}'.format(self.title, self.content, self.created_at)

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    image_url = request.GET.get('image_url')
    
    # DB에 저장하기
    # 위에서 실행했던 방식과 똑같이 하면 된다!!
    article = Article()
    article.title = title
    article.content = content
    article.image_url = image_url
    article.save()
   
    context = {
        'title': title,
        'content': content,
        'image_url': image_url,
        'created_at': article.created_at,
    }

    # 다 끝나면 페이지를 랜더하지 말고... 돌려줄 거란 뜻으로.. redirect를 하자. import하는 거 잊지 말고
    # 메인 문지기를 통해 루트의 별명을 지어주고, 이 안에 별명을 넣어주자.
    return redirect('index')
    # return render(request, 'create.html', context)

def index(request):
    # 지금까지 작성된 모든 글을 보여주자.
    # root가 되는 친구'
    
    # DB에서 가져오자
    articles = Article.objects.all() # 리스트랑 비슷하게 생긴 쿼리셋 객체
    # 순서를 바꾸려면??

    context = {
        'articles': reversed(articles), # reversed로 뒤집어도 되긴 한다. 나중에 orderby를 사용하게 된다. 
    }
    return render(request,'index.html', context)
