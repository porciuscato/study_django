# 10월 21일

## Auth

오늘의 테마

- 회원가입
- 로그인

++ `권한관리`까지

회원가입과 로그인을 묶어서 `Authentication`

회원가입과 로그인 프로세스가 우선

회원가입의 모습은? 

User 모델을 구성하면.... email, password, password confirmation, name 등등

이들을 Auth 모듈이라 부름



가입 됐다는 건, DB에 담는 것과 같다.

회원가입은 실제로는  User라고 하는 DB에 대한 CRUD와 똑같다!!

저장된 회원를 기반으로, 사람을 인증하는 것.

Http의 장점이자 단점은... stateless : 무상태성? -> 상태를 보관하지 않는다는 뜻인데, http는 그저 요청과 응답의 한 번으로 끝나는 것. 그렇기 때문에 로그인 정보는 어렵다. 요청에 대한 응답을 한번씩만 보내주는데 로그인에 대한 정보를 가지고 있어야 하는 것

이 사람이 이전에 뭘 했고 어떻게 들어왔는지 트래킹을 함.

`무상태적인 프로토콜 위에서 과연 어떻게 상태를 저장할 것인가?`

- cookie
- session(cache)

로그인의 본질이란....

특정인이 철수임을 알기 위해... http만으로는 이 사람이 철수인지 알 수 없다.

철수임을 추적하기 위해... 서버가 철수의 요청에 응답을 보낼 때 쿠키(과자부스러기)를 보낸다.

매번 철수가 특정한 서비스에서 보내면 쿠키를 보내도록 만든다.



쿠키는 보안 이슈 때문에 로그인에서는 안 씀

- 쿠키의 취약점: 한 번 쿠키가 묻으면, 그 이후에 보내는 모든 request에 쿠키가 묻어서 감. 만약 다른 사람의 쿠키를 브라우저에 넣으면 그 사람이 됨
  - 그래서 거의 쓰이지 않음. 그럼에도 쿠키는 무의미하지는 않다. 광고, 쿠팡(로그인 안 해도 장바구니에 저장되어있다.)



서버가 클라이언트에게 보내는 과자 부스러기. 이 쿠키들이 다음 요청 땐 실려서 나간다. 

쿠팡이 과자 부스러기를 남겨놓으면 페북이 쿠키를 보고 마땅한 광고를 보여줌



이 프로토콜의 약점으로 로그인을 속일 수 있음

그래서.. 쿠키만 가지고 판단하는 것이 아니라, 서버 컴퓨터에 알게 모르게 로그인 유저에 대한 정보를 담기 시작.

접속된 유저들의 리스트가 나오고... 이 접속된 유저에 대한 IP, MAC.Cookie 등을 관리하는 session을 만들고 이들의 정보가 일치해야만 정보를 보내주는 것. -> 특정 기간에만 살아있는 데이터들



-> 결국 이들은 http가 stateless하기 때문에 쓰는 것

웹 했다고 하면 기술 면접에서 가장 만만하게 나오는 용어



----



#### 장고 auth 모듈을 사용해서 만들어보자

장고는 sessionid를 쿠키로 쓴다.

회원가입은 user, acounts라는 모델을 만들어서 CRUD임

```python
python manage.py startapp accounts
```

반드시 `accounts` 를 써야 함

article 했던 것과 회원가입은 실제로는 같다.

Abstract(요약 정보)

AbstarctBaseUser(핵필수) -> AbstractUser(일반적인) -> User

이렇게 다단계로 잘 쪼개 놓을수록 커스터마이징이 쉽다.



나중에 AbstarctBaseUser만 가지고 커스터마이징한 유저를 만들 수 있다.

이 클래스 안에 우리에게 필요한 것들을 만들 수 있다. 이것들을 다단으로 해놓지 않으면 커스터마이징하기가 어렵다.

form의 action을 삭제해도 자기 자신에게 보내기 때문에 

삭제하면 자기자신에게 감

```html
{% extends 'base.html' %}
{% load bootstrap4 %}

{% block body %}

<div class="container">
    <h1>회원가입</h1>
  <form method='POST'>
    {% csrf_token %}
    {% bootstrap_form form %}
    <button class='btn btn-success' type='submit'>제출</button>
    {% buttons submit='회원가입' %}{% endbuttons %}
  </form>
</div>


{% endblock %}
```



embed() 창 실행

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from IPython import embed

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # 실제 DB에 정보 저장
        form = UserCreationForm(request.POST)
        embed()
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)
```

`form.as_p()`

`form.is_valid()`



UserCreationForm(회원가입용) & AuthenticationForm(로그인용)

- ModelForm
- UserCreationForm -> User에 대한 **C**RUD
- AuthenticationForm -> Session에 대한 **C**RU**D**
  - 접속된 유저에 대한 정보를 가지고 있어야 한다. 
  - 데이터베이스는 아님



-> session 도 CRUD 형태로 간다.



로그인을 직접 짜는 것은 상당히 위험

표준적으로 잘 짜여져 있는 걸 쓰는 게 좋음



그런데 로그인을 한 뒤에도 로그인이 뜨면 안 됨

로그아웃을 한다는 것은 session을 지우는 것

손수 지우는 것이 아니라... 



로그인이 되야지만 글을 쓸 수 있게 만들어야 한다.

세션 creation을 하는 것



request는 connectionless



next에 다음 장소를 지정하더라도 next로 안 간다.



request.GET.get('next') : 는 그저 이 안에 담긴 url을 대신 쓰는 것에 불과



---

POST로 요청 들어옴 -> 로그인 검증 -> next로 redirect(GET) : 이때 들어오는 요청이 GET이기 때문에



탈퇴





# 10월 22일

https://www.youtube.com/watch?v=OpoVuwxGRDI

https://jeong-pro.tistory.com/80

쿠키, 세션, 캐시

-> 이 차이에 대해 알아보자



### 쿠키 세션 캐시

#### 쿠키 

- 쿠키 기본
  - 사이트에 방문할 때 내 브라우저에 기록되는 정보 (내가 가진 정보)
  - 담는 정보
    - 이름, 값, 만료날짜(쿠키 저장기간), 경로 정보 등등
  - 쿠키는 일정시간동안 데이터를 저장할 수 있다(로그인 상태 유지에 활용)
  - 클라이언트의 상태 정보를 로컬(브라우저)에 저장하고 참조하는 것이 쿠키
- 쿠키의 프로세스
  - 브라우저가 웹페이지에 접속 -> 웹페이지를 받으면 쿠키를 로컬에 저장 -> 서버에 재요청을 보낼 때 웹페이지 요청과 쿠키도 함께 전송(마치 지속적으로 로그인 정보를 가지고 있는 것처럼 사용)
- 쿠키의 한계
  - 사용자가 임의로 수정이 가능
  - 남이 사용하기도 용이
- 사용처
  - 로그인 아이디 정보, 장바구니에 담기는 물건들 등등
  - 지워지거나 조작되어도 별 일 없는 정보들 -> 이런 것들을 브라우저에 저장

#### 세션

- 세션 기본
  - 일정 시간 동안 같은 브라우저로부터 들어오는 일련의 요구를 하나의 상태로 보고 그 상태를 유지하는 기술
    - request를 보내면 서버 엔진이 클라이언트에게 유일한 ID를 부여하는데 이것이 세션 ID
  - 쿠키들이 관리하기 어려운 정보들은 세션에서 관리
  - 서버에서 사용자, 브라우저에게 키를 하나 보내고 사용자는 이를 쿠키에 저장
    - http요청을 보낼 때 이 키를 함께 전송 -> 그러면 서버는 사용자임을 인식
  - 중요한 정보들은 서버에서 관리 -> 이를 세션이라 함
- 세션 프로세스
  - 서버는 클라이언트의 요청이 들어오면 세션 ID를 발급 -> 

#### 캐시

- 가져오는데 비용이 드는 데이터를 한 번 가져온 뒤에 임시로 저장해두는 것
- 가령
  - 이미지, css, js 파일 등 사용자의 브라우저에 저장 -> 한번 캐시에 저장되면 서버가 아닌 브라우저를 참고. 그렇기에 서버에서 변경되어도 사용자는 변경되지 않을 수 있음. 그래서 캐시를 지워주거나 서버에서 응답을 보낼 때 header에 캐시 만료시간을 명시하는 방법을 사용

#### 쿠키와 세션의 차이

+++ 저장위치

- 쿠키는 클라이언트 측에서 파일로 저장
- 세션은 서버에 저장

+++ 라이프 사이클

- 쿠키는 만료시간이 있지만 파일로 저장되기에 브라우저를 종료해도 정보가 남아있을 수 있음. 또한 만료 기간을 넉넉하게 잡으면 쿠키 삭제를 할 때까지 유지될 수 있음
- 세션도 만료시간을 정할 수 있지만 브라우저가 종료되면 만료시간에 상관없이 삭제됨

+++ 속도

- 쿠키로 인해 서버에 요청을 보낼 때 속도가 빨라진다.
- 세션은 정보가 서버에 있기 때문에 처리로 인한 시간 지연이 생긴다. 비교적 느린 편





-- client에서 server로 request를 보낼 때

request는 header와 body(content) 파트로 나눠져 있음

header 에는 method, host, protocol 을 담음

body는 html, json 등등을 보냄



과자 부스러기 던져보기

cookie는 key-value 타입

```python
def send_cookie(request):
    res = HttpResponse('과자 받아라')
    res.set_cookie('mycookie', 'oreo')
    return res
```



쿠키와 세션의 비교

- 로그인에 사용되지만, 



쿠키와 세션이 나오는 이유가 애초에 브라우저가 connectionless 이고 stateless이기 때문

쿠키, 세션, (캐시)의 비교



브라우저의 캐싱? 

- static file 들 : css, js



쿠키와 세션을 사용하는 이유?

브라우저의 특징이자 단점을 보완하기 위해(비연결성, 비상태성)





크롬(크롬 한정)은 sqlite를 사용하여 쿠키를 사용.

우리가 쿠키의 유통기한까지 정할 수 있음



세션



++++ middleware란?

user....

어떤 특정 기능이 있을 때, 비밀번호나 암호나 서버 등을 직접 다루지 않고 중간 매개를 사용 -> ORM, DTL 등등이 모두 미들웨어. 나랑 DB사이에 껴있고 나랑 template 사이에 껴있는 

세션을 구현하는 여러가지 방법 -> 파일로 만들 수 있고

세션은 file based session, data based session 등. 

너무 헤비하다보니, 가장 가벼운 cookie based session을 사용



브라우저 쿠키에 대한 정보를 서버에서 세션으로 관리

방문 횟수를 세션으로 만들어보자



폰에는 광고ID가 있어서 쿠키에 저장하지 않는다.



​	

form은 어떻게 수정할까?

-> 상속을 받아서 커스터마이징

유저는 어떻게?

 https://docs.djangoproject.com/ko/2.2/topics/auth/customizing/#referencing-the-user-model 





비밀번호 수정은 약간 까다롭다.



M : N

뭐가 있을까?

ex) 수강신청, 예약(진료, 미용 등등), 좋아요, 팔로우

왜 1 대 N이 어려울까?

has-many / belongs-to

Article은 Comment를 포함하는 관계

그런데 수강신청에 대해 생각해보자

- Course가 있고, Student가 있다. 학교에 여러 수업이 있다. 알고리즘, 언어, OS 등등 수업이 있다. 학생은 A, B, C 등등. 모두가 모든 걸 다 들을 수 있다.

  - 1대 N 에서는 모든 것이 하나의 글에 속함
  - 그러나 위의 관계에서는 서로가 서로를 많이 가진다. 한 글이 많은 사람들에게 좋아요를 받을 수 있고, 한 사람이 많은 글을 좋아할 수 있다.

  => 이때 엑셀로 표현하면 간단하다.



그래서 M 대 N의 관계는 테이블 2개로 표현할 수가 없다.

`그래서 Like라는 새로운 테이블을 만든다!!`

user가 글을 좋아한다고 했을 때, 주어와 목적어 사이에 동사 테이블을 만든다. 혹은 중계 테이블, 조인 테이블 등등

그래서 user / like / article 이라는 구조로 만든다.

like는 user_id와 article_id를 칼럼으로 가진다.

| user_id | pk   | article_id |
| ------- | ---- | ---------- |
| 1       | 1    | 1          |
| 1       | 2    | 2          |
| 2       | 3    | 1          |
| 2       | 4    | 2          |
| 3       | 5    | 1          |
| 3       | 6    | 2          |

그런데 follow의 느낌은 살짝 다르다.

1 대 N

M 대 N

M 대 N 이면서 self-referencing



장고한테 또 맡길 거다.

user랑 article이랑 M 대 N의 관계를 맺으니까 알아서 하라고 만듦

대부분 목적어에 달아준다.

```python
like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
```





```python
In [20]: article.like_users.all()
Out[20]: <QuerySet [<User: mpcato>]>

In [21]: mpcato.like_articles.add(Article.objects.get(pk=11))

In [22]: mpcato.like_articles.all()
Out[22]: <QuerySet [<Article: 장고 form>, <Article: 과연? 수정되나?>]>

In [23]: mpcato.like_articles.add(Article.objects.get(pk=11))

In [24]: mpcato.like_articles.all()
Out[24]: <QuerySet [<Article: 장고 form>, <Article: 과연? 수정되나?>]>

In [25]: mpcato.like_articles.remove(article)

In [26]: mpcato.like_articles.all()
Out[26]: <QuerySet [<Article: 장고 form>]>

In [27]: jisoo = User.objects.last()

In [28]: jisoo
Out[28]: <User: jisoo>

In [29]: article.like_users.add(jisoo)

In [30]: article.like_users.all()
Out[30]: <QuerySet [<User: jisoo>]>
    
In [31]: article.like_users.count()
Out[31]: 1
```





<a href="/articles/:id/like/"></a>