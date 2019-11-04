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



# 10월 23일

- 게시글에 댓글 달고 좋아요까지! 자유롭게

- DTL에서는 함수를 호출하더라도 변수를 부르듯이 쓴다. (DTL은 파이썬이 아니다)

DB쿼리는 자주 호출하면 좋지 않다. 효율이 엄청 떨어진다.

`exist()`

filter 는 SQL의 where과 같다.

ORM: .get() vs .filter()

- get은 한 개 뽑을 때(LIMIT 1) -> 없을 때 에러가 발생하고
- filter는 여러 개 뽑을 때 -> 없을 때 빈 쿼리 셋이 나온다(굳이 에러 핸들링 하지 말고 빈 쿼리셋을 다루는 게 낫다.)

.exist() -> 필터를 줘서 가는 것 (이 쿼리 셋 안에 뭐라고 있니? 라고 물어보는 것)



이런 코드가 문제일 수 있다.

```html
<p>좋아요 : {{ article.like_users.count }}개 </p>
<p>좋아하는 사람 : 
  {% for arti in article.like_users.all %}
    {{ arti }}
  {% endfor %}
```

 굉장히 안 좋은 코드다. 비용이 크다.  all이 매번 불리게 된다. 불릴 때마다 DB에 쿼리를 보낸다 -> 그러므로 캐싱을 해야

#### 캐싱

with context 

with template tag

```html
{% with total=business.employees.count %}
    {{ total }} employee{{ total|pluralize }}
{% endwith %}
```



```hrml
<p>좋아요 : {{ article.like_users.count }}개 </p>
<p>좋아하는 사람 :
  {% with likers=article.like_users.all %} 
    {% for liker in likers %}
      {{ liker }}
    {% endfor %}
  {% endwith %}
```

-> 이로 인해 all은 한 번만 불리게 되었다!! -> 성능 대폭 개선



### 프로필 만들기



팔로우 만들기

`User` follws `User`

id(pk) / from_user_id / to_user_id

팔로우 기능을 만들기 위해 새로 모델을 정의함!



원래 바인딩 되어있던 칼럼을 고치는 건 상당히 위험

모델 디자인...



팔로우

url 디자인

```html
<a href="/accounts/follow/1">팔로우</a>
```





```
기획
http://trello.com/
https://www.notion.so/
.
디자인
https://www.figma.com/
.
사진
https://unsplash.com
.
코드 에디터
https://code.visualstudio.com/
.
CSS 라이브러리
https://tailwindcss.com
https://bulma.io
.
깃 저장소
https://github.com/
https://about.gitlab.com/
https://bitbucket.org/product
.
클라이언트
https://insomnia.rest  (REST)
https://altair.sirmuel.design (GraphQL)
.
검색엔진
https://www.algolia.com
.
유저 비밀번호 관리
https://auth0.com/
https://aws.amazon.com/ko/cognito/
.
이메일
https://www.mailgun.com/
https://mailchimp.com
.
SSL Certificate
https://letsencrypt.org/
.
백엔드
https://www.heroku.com/
https://aws.amazon.com/
.
프론트엔드
https://pages.github.com/
https://www.netlify.com/
.
서버리스
https://aws.amazon.com/lambda/
https://cloud.google.com/functions/
.
데이터베이스,
https://aws.amazon.com/dynamodb/
https://cloud.google.com/firestore/
https://www.mongodb.com/cloud/atlas
https://fauna.com/
.
파일 업로드
https://cloud.google.com/storage/
https://cloudinary.com/
.
에러 리포팅
https://sentry.io
.
채팅
https://pusher.com
.
푸쉬알림
https://onesignal.com/
.
피드
getstream.io
.
분석
analytics.google.com/
https://www.hotjar.com
https://mixpanel.com/
.
시간관리
https://wakatime.com/
```

 https://thevc.kr/ 



### 해시태그

태그는 한 테이블에 다 모아서 manyTomany 관계를 가질 수 있다.



ORM의 장단점은?

- lazyloading? : 코드가 쓰여지자마자 바로 DB에 쿼리를 보내지 않는다. 해당하는 코드가 돌아갈 때, fetch에 이르러 한 번만 요청함. 
  - 그래서 오히려 ORM에 의존하는 것이 더 유리하기도 하다. 
  - with 를 쓰지 않더라도 호출이 한 번만 이뤄지기 때문에 성능에서 크게 차이나지 않는다.

 http://raccoonyy.github.io/using-django-querysets-effectively-translate/ 

도널드 크누스





# 10월 24일

- Gravatar



서버사이드 앱과 앱이 배포되는 과정에서 front-end를 담당하는 서버가 분리되기 시작.

SPA(single page aplication) : 페이지 로드 없이 사용 (react, view, angular 등 덕분에 유명해짐)

이것들만 돌려주는 프런트앤드 서버만 따로 만듬(경량형 서버를 사용. MERN(몽고 DB - json의 데이터베이스화)(익스프레스), (리엑트), (Node.js - 사실은 자바스크립트))



NoSQL

RDBMS는 스키마가 있어야 한다. 그런데 NoSQL은 비정형 데이터처럼, json 파일 하나를 데이터베이스처럼 씀. 이를 Document라고 함.

트위터 등을 관계형 데이터로 사용하다보니 칼럼이 너무나 많아졌음. 그래서 write를 빠르게 할 수 있는 방법을 찾던 중... 글 하나하나를 빠르게 만드는 방법으로 NoSQL이 유명해짐



template이 분리가 된...



MSA
왜 점점 자바가 효용 가치가 잃어가는가... 가장 적합한 언어를 쓰는게 좋은데.. 데이터 분석이 파이썬으로 이루어지기 때문. 

여러 가지 언어가 쓰임. 각 환경이나 프로그램에 적합한 언어를 쓸 수 있어야 한다. 

어디로 가는지에 따라 뭘 배우는지가 달라진다...



이제 우리는... 장고를 API 서버로만 바꾸게 될 것. 복잡한 DB 구성은 장고에게 맡기고 템플릿 단계에서는 자바 스크립트에게 넘겨줄 것

장고로 그걸 어떻게 해야할지 보게 될 것



### API 서버 만들기

- django rest framework 다운받기

```
pip install djangorestframework
```

django DRF

 https://www.django-rest-framework.org/ 

settings.py 에 추가할 땐

```python
INSTALLED_APPS = [
    'rest_framework',
    'django.contrib.admin',
    ....
]
```

지금까지는 settings.py에 앱 이름을 그냥 추가했었는데...

```python
'musics.apps.MusicsConfig',
```

이젠 이런 식으로 해보자.

dummy data





dumping 하는 방법?

`python manage.py dumpdata music > dummy.json`

- 우린 이미 json 파일을 가지고 있으니까..

  `python manage.py loaddata musics/dummy.json`

  - 이것의 반대 방향이 dumpdata

  가령(데이터 베이스에 있는 자료를 json 파일로 만듦)

  `python manage.py dumpdata articles > dummy.json --indent 2`

  하면 json 파일로 받을 수 있음

  이것이 덤핑

  이제는 요청이 들어오면 json 파일로 보내보자

  

요청이 들어올 때 html이 아니라 json 파일을 덤핑하려면?



article의 상세 페이지처럼..



#### API 자동 완성 : yasg

API는 반드시 문서가 잘 만들어져야 함 -> 그런데 귀찮으니까 API를 자동으로 만들어주는 툴이 있음

 https://github.com/axnsan12/drf-yasg 

`pip install drf-yasg`





RESTful API

#### Music : Comment  = 1 : N

##### Music REST API

| C         | POST   | /music/    |
| --------- | ------ | ---------- |
| R(list)   | GET    | /music/    |
| R(detail) | GET    | /music/:pk |
| U         | PUT    | /music/:pk |
| D         | DELETE | /music/:pk |

##### Comment REST API

| C         | POST   | /music/:pk/comments     |
| --------- | ------ | ----------------------- |
| R(list)   | GET    | /music/:pk/comments     |
| R(detail) | GET    | /music/:pk/comments/:pk |
| U         | PUT    | /music/:pk/comments/:pk |
| D         | DELETE | /music/:pk/comments/:pk |

url에는 목적어만 나와있고 동사는 POST, GET 등으로 빠져있다.





페이스북은 url을 그래프ql. graphQL

url을 쿼리 문장으로 바꾼다!

요청을 보낼 때 json으로 보냄

payload

url 만으로는 파악하기 어려워서 payload도 확인을 해야 서버에 어떤 요청이 가는지 알 수 있다.



포스트맨

 https://www.getpostman.com/downloads/ 

get 요청이 아닌 post나 put 요청은 브라우저로 할 수 없어서 포스트맨을 사용한다.





```
<월말 공지>
• Django 프로젝트가 주어지며, 문제에 제시된 기능을 구현합니다.
범위는 다음과 같으며, 기능에 필요한 예외처리를 포함하여 구현 하여야 합니다.
1. 게시글 CRUD 및 댓글 작성
2. 회원가입 및 로그인/로그아웃
3. 좋아요 기능
단, 기능 구현시 CSS로 꾸미거나 하는 내용은 없습니다.
•  아래의 사항은 모두 금지 합니다.
1. 시험 문제와 무관한 소스코드 작성 (HTML, CSS 포함)
2. django를 제외한 pip 패키지 사용
3. visual studio code 이외의 환경 사용 및 추가 확장 프로그램(extension) 설치 (sqlite는 가능) (edited) 
```













---















### 월욜 과목평가

sql은 pdf위주로

**<과목평가 공지>**
• SQL (슬라이드 전범위)
• Django ORM (쿼리 및 현재까지 배운 모든 내용) (edited) 

SQL & ORM : https://gist.github.com/edu-john/cd8fa1016093ab06583d44cf0388e22e (edited) 

ORM & Relation : https://gist.github.com/edu-john/34772fa8b4ecb22d86e92d90d4acef63



그냥 쉘은 다 불러와야 한다.

쉘 플러스는 알아서 다 import 해준다.



중개모델을 쓰게 되면 불편한 점??

중개모델 없이 쓰는 법을 익히자





# fixture

- 미리 만들어놓은 json 파일을 db에 적용시키자.

- 방법

  - 먼저 DB를 만든다.

  - json 파일이 가지고 있는 모델명에 해당하는 app에 fixtures 폴더를 만든다.

    ```json
    // 가령 이 데이터는 model이 Movie이기 때문에 movies에서 정의한 Moive 모델과 맞추기 위해 movies 앱 하부에 fixture 폴더를 만들도록 한다.
    {
            "pk": 10,
            "model": "movies.Movie",
            "fields": {
                "title": "터미네이터2 3D",
                "audience": 11744,
                "poster_url": "https://movie-phinf.pstatic.net/20191010_99/1570669194041iWfdl_JPEG/movie_image.jpg",
                "description": "인간과 기계의 대전쟁.. 그를 지키지 않으면 미래 또한 없다!\n미래, 인류와 기계의 전쟁은 계속 되는 가운데 스카이넷은 인류 저항군 사령관 존 코너를 없애기 위해 액체 금속형 로봇인 T-1000을 과거의 어린 존 코너에게로 보낸다. 미래의 인류 운명을 쥔 어린 존 코너. 스카이넷의 T-1000은 거침없이 숨 가쁜 추격을 시작하는데…",
                "genre_id": 8
            }
        }
    ```

  - 이 안에 DB에 넣을 json 파일을 넣는다.

  - load 명령어를 입력한다.

    ```shell
    $ python manage.py loaddata genre.json
    $ python manage.py loaddata movie.json
    ```

    

    