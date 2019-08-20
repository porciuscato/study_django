from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    # table 형태로 게시판을 보여줌
    
    posts = Post.objects.all()

    context = {
        # DB에 있는 모든 데이터
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

def new(request):    
    return render(request, 'posts/new.html')

def create(request):
    # new에서 날아온 데이터로 DB에 저장한다.
    # post = Post(
    #     title = request.GET.get('title'),
    #     content = request.GET.get('content'),
    #     img_url = request.GET.get('img_url'),
    # )
    # post.save()
    
    # save가 해주는 역할은? validation을 한다. `데이터 유효성 검사`. 정수가 들어갈 곳에 잘못된 값이 들어가있는지 검사하는 것
    # 나중에 이에 대한 조건문을 쓰게 될 것

    # create()을 하면 데이터 유효성 검사가 안 이루어짐
    Post.objects.create(
        title = request.GET.get('title'),
        content = request.GET.get('content'),
        img_url = request.GET.get('img_url'),        
    )

    # one-line으로 정리
    # Post.objects.create(**request.GET) request.GET는 딕셔너리는 아니지만 딕셔너리와 비슷
    # request.GET을 펼쳐버리면 {'title': 내용, 'content': 내용} -> 태그에 들어가는 name을 같게 만들면 이처럼 한 번에 가능하다.
    # 그러나 이런 방식은 요새 비추. 어떤 데이터를 가져왔는지 알 수 없어서.
    # 불순 데이터가 있을 수도 있기 때문. 가려내기가 어렵다.
    return redirect('home')

def detail(request, pk):
    # pk라는 id를 가진 글을 찾아와 보여준다.
    post = Post.objects.get(id=pk)
    # (pk=pk)로 써도 된다.
    # coloumn 명이 먼저 온다.
    # get은 id 뿐 아니라 다른 정보도 가져올 수 있다.
    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)

def delete(request, pk):
    # pk라는 id를 가진 글을 삭제한다.
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('home')

def edit(request, pk):
    # pk라는 id를 가진 글을 편집하게 함
    # 1. pk라는 id를 가진 글을 찾는다.
    post = Post.objects.get(pk=pk)
    context = {
        'post' : post,
    }
    return render(request, 'posts/edit.html', context)

def update(request, pk):
    # 1. pk라는 아이디를 가진 글을 찾아서
    # 2. /edit/으로 부터 날아온 데이터를 적용하여 변경함

    post = Post.objects.get(pk=pk)
    post.title = request.GET.get('title')
    post.content = request.GET.get('content')
    post.img_url = request.GET.get('img_url')
    post.save()

    # return redirect(f'/posts/{pk}/')
    return redirect('posts:detail', pk)
