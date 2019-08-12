# django

## 8월 12일

flask로 했던 것을 django로 옮기는 과정.

- 인기있는 프레임워크

  `hotframeworks.com`

- Ruby on rails 만든 dhh 형아. 돈 많은 형아



파이썬 들어가있으면 웹은 장고로 만들어졌다고 생각하면 된다.

user/login/ 처럼 끝에 `/` 가 들어가 있으면 django라고 보면 됨



프레임워크가 규칙을 만들어뒀는데..

- 대체로 독선적인 프레임워크들의 느낌은.... 초반에 배워야될 것이 있는데 배우고 나면 그 이후에 편해짐

- 프레임워크가 규칙을 만들어놓지 않으면... 초반엔 쉽지만, 어드밴스드한 기능을 붙여놓기가 어려워지고 유지 보수가 갈수록어려워진다.



장고는 다소 독선적





그동안 배포했던 웹은 static web

우리는 Dynamic Web을 만들 것.  (Web Application Program)



Web App을 만드는 것은 카페를 만드는 것

- 바닥부터 하려면....?
  - 웹도 마찬가지. 바닥부터 만들어도 됨. 그러나 대체로 그런 카페들은....음.... 오케이. 생각보다 유지보수가 어렵다

- 프랜차이즈 창업을 하듯
  - 프레임워크를 사용하는 것과 같은 논리
  - 기본적인 건 알아서 해줄테니 넌 그냥 좋은 카페를 만드는 거에 집중해!
  - 넌 그냥 좋은 웹 서비스 만드는 거에 집중하라고!



- 언어별로 프레임워크가 있는데... 파이썬은 장고
  - 장고를 쓰는 사이트는 엄청나게 많다.
  - 네이버는 팀마다 프레임워크를 다르게 만든다. 일반적인 대기업보다는 네이버가 많은 시도를 한다. 



우리는 웹 서비스를 만드는 것

웹의 패턴은 요청과 응답으로 이루어져 있다.

```python
@app.route(url(주문서)):
    def index():
        return render_template()
```

그런데 이런 요청이 엄청나게 많아지면? 반복되는 패턴이 생성되면?

post로 엮이는 건 하나로 묶으면 좋을 듯

flask를 통해 큰 형태의 서비스를 만들다보면 코드 유지관리가 어려워진다...



프레임워크를 만들 때 시스템이 있으면 좋겠다... 그걸 아키텍쳐라고 하는데 그것은 하나의 패턴. 코드를 어떤 형태로 구성해서 쓸지..

MVC 라는 패턴이 아름답게 유지가 됨 -> ASP.NET MVC....프론트앤드 단에서는 거의 다 씀



장고는.... 좀 똘끼 넘치는 아이? 만드는 사람들이 관종이라 MVC가 아닌 MTV로 부름

장고를 이루는 삼바리 MTV.



### MTV

가장 중요한 친구는 V다.

V가 모델과 템플릿을 관리하는 걸로 되어있다.

- M: model - 데이터를 관리
- T:  Template - 사용자가 보는 화면 (html을 만들어주는 것)
- V: 중간관리자.



V 라는 친구가 항상 관리

어떻게 통제하는가?

- 웹 기반 강의 사이트를 예로 들자
  - 1번 강의를 보고 싶다고 요청을 보내면 V가 받는다. (앞에 문지기가 한 명 더 있음(url 관리자))
  - V가 전달받고 M한테 데이터를 찾으라고 요청.
  - M은 찾은 뒤 V 한테 넘겨줌
  - 유저는 html을 통해 봐야하기 때문에, T가 HTML을 만들어서 사용자에게 보냄

다른 곳에서는 MVC 라고 하지만 장고는 MTV라고 함









듀랑고 사건.... 파이썬 2로 만들어졌지만 사용할 수 있는 사람들이 모두 나가고... 유지보수가 안 되는 현상 발생

특정한 언어 조차도 버전을 바꿔서 프로젝트 별로 관리해야 한다. 가상환경을 사용하면 좋다.

`venv` : 가상환경을 시작할 때 쓰는 명령어





### 장고 설치

최신 버전을 쓰즈아

`pip install django`



보일러 템플릿, 스타터 템플릿

`django-admin startproject first_app .` : first_app 은 우리 프로젝트 이름 `.` 은 현재 폴더를 지칭



`django-admin startproject [프로젝트 이름] [경로]`



#### django 할 때 convention

- 폴더의 이름은 대문자로 `FIRST_APP` (프로젝트 구분 폴더)

- 일한 이름의 폴더가 소문자로 들어가게 될 것



옮기는 git 명령어는 `mv`

rename  할 때도 `mv`



`python manage.py runserver`

`localhost:8000` : 서버가 돌아가고 있다는 것! `ctl C ` 누르면 꺼짐

 으로 들어가면 달라진 것이 보임





`setting.py`가 중요

모든 세팅들이 들어있음

`urls.py`도 중요. 가장 많이 쓰는 파일



`manage.py`는 거의 건드릴 일 없다.



#### 우리 첫번째 로직을 만들기 위해 앱을 하나 설치하자?



#### 장고에 대한 이해

전체 프로젝트는 Project라는 이름으로 불리고 이 안에 세부적인 app들이 들어오게 됨

이 앱들은 하나하나가 다른 역할을 가짐. 하나는 게시판 앱이 될 수 있고, 하나는 회원관리 앱이 될 수 있고, 하나는 영화평점 앱이 될 수 있다.

로직 별로 앱을 구분해서 쓰는 것이 장고의 패턴이다.



그러면 깔아보자

`python manage.py startapp pages `

- `	python manage.py startapp [앱이름] ` 

이렇게 하면 파일이 하나가 더 생김

`pages` 라는 폴더가 생김



views.py가 v를 담당

중요한 건

m이랑 v

이 두 파일이 아주 중요



장고에는 urls.py라는 문지기가 있음

urls.py에 통과시킬 주문을 넣지를 않으면 아예 통과를 안 시킴



플라스크에서는 요청을 app.route() 안에 넣었는데 장고에서는 파일 별로 분리되어 있다.

안에서 무엇을 할 지 함수로 정의를 해놨었는데 이것은 views.py로 분리 되었다.



문지기를 거쳐서 view를 거치고 템플릿을 가게 되는 패턴. 이것이 오늘 하게 될 일



문지기한테 앱을 등록하고, 해당하는 요청이 오면 v한테 넘기고 t에게 넘기면 t가 사용자에게 전달



#### 페이지를 바로 만들어보자

먼저 문지기에게 말해줘라

앞으로 주문서의 경로가 이런 식으로 될 거야 라고 알려줘야 함

`urlpatters` 리스트 안에 넣어줌

```python
urlpatterns = [
    # path 함수는 
    # 첫번째 인자 : 주문서(url 경로)
    # 두번째 인자 : view 함수의 위치
    path('admin/', admin.site.urls),
    path('index/')
]
```

```python
urlpatterns = [
    # path 함수는 
    # 첫번째 인자 : 주문서(url 경로)
    # 두번째 인자 : view 함수의 위치
    path('admin/', admin.site.urls),
    # pages 앱 안에 있는 index를 찾아가라
    path('index/', pages.index),
    # 장고는 trailing comma를 붙이는 것이 컨벤션. 지금까지는 안 썼음
]
```

comma를 붙이면 편함. 이미 콤마가 있으면 바로 요소를 넣어두면 됨



pages 가 어디 있는지 명확히 알려줘야 함

새로운 앱이 왔다는 것을 setting.py에 알려야 함

setting.py의 installed_apps에 알려줘야 함

우리가 설치할 앱은 최상단에 올려주자

```python
INSTALLED_APPS = [
    'pages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



이제는 우리가 이 앱을 쓸 수 있음

```python
from pages import views
이걸 써 줘야
```

이제는 views.index로 써주자

```python
urlpatterns = [
    # path 함수는 
    # 첫번째 인자 : 주문서(url 경로)
    # 두번째 인자 : view 함수의 위치
    path('admin/', admin.site.urls),
    # pages 앱 안에 있는 index를 찾아가라
    path('index/', views.index),
    # 장고는 trailing comma를 붙이는 것이 컨벤션. 지금까지는 안 썼음
]
```



f1을 누르고 select interpreter를 누르고 virtual 환경에서 설정



views.py에 들어가서 

플라스크의 함수 부분을 만들어주었듯이 만들어야 함.

우리가 위에서 views.index라고 했으니 index 함수를 만들어줌

이때 항상 request라는 인자를 넣어주어야 함

```python
def index(requset):
```



플라스크처럼 문자열을 반환할 수 있을까?

```python
def index(requset):
    return 'hello'
```

우리가 아무것도 만들어주지 않으면 기본 페이지가 뜨는데 우리가 앱을 만들었으므로 

응 안 됨



이렇게 해야

```python
def index(request):
    # request는 사용자가 보내온 인자들을 전달. 사용자가 보낸 요청들
    # 반드시 맨 앞에 request 인자를 보내야 함
    return render(request, 'index.html')
```



그리고 pages폴더 안에 templates 폴더를 만들고 index.html을 만든다. 그러면 이걸 전달하게 됨





다시 로직 별로 따라가보자

first_app의 메인 폴더 아래에 urls.py가 문지기가 됨.

새로운 걸 하게 되면 path함수를 통해 새로 알려주면 됨



```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('home/',views.home),
]

##############################################
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # request는 사용자가 보내온 인자들을 전달. 사용자가 보낸 요청들
    return render(request, 'index.html')


def home(request):
    return HttpResponse('홈페이지')
```



사실 궁극적으로 전달되는 것은 HttpResponse의 객체

html을 넘기는 것이 아니다.



```python
def home(request):
    return HttpResponse('<h1>홈페이지</h1>')
```

이것도 되긴 함



```python
def index(request):
    return render(request, 'index.html')
```

render 함수는 httpresponse 객체를 리턴 한다.



*** 전달하려는 html파일은 어플 이름으로 된 디렉터리 안에 templates라는 디렉터리를 만들고 이 안에서 생성되어야 한다.



### 장고 템플릿 랭귀지 DTL(django template language)

넘겨줄 인자를 딕셔너리로 넘기면 됨

```python
def home(request):
    # return HttpResponse('<h1>홈페이지</h1>')
    name = '이수진'
    data =['강동주','김지수','정의진']
    # return render(request, 'home.html',name=name,data=data) 이게 아니라
    return render(request, 'home.html',{'name': data}) # 이런 식으로 하면 됨
```

```html
<h1>데이터를 넘겨 받는 법</h1>
<h2>{{name}}</h2>
```

이런 식으로 `딕셔너리`로서 전달하자.

```python
def home(request):
    name = '이수진'
    data =['강동주','김지수','정의진']
    context = {
        'name': name,
        'data': data,
    }
    return render(request, 'home.html',context)
```



html에서 for문을 돌릴 수도 있다.

```html
<body>
  <h1>데이터를 넘겨 받는 법</h1>
  <h2>{{name}}</h2>
  {% for item in data %}
  <p>{{item}}</p>
  {% endfor %}
</body>
```





#### flask 때처럼 lotto 번호를 출력해보자.

1. urls.py

   ```python
   urlpatterns = [
       path('admin/', admin.site.urls),  
       path('index/', views.index),
       path('home/',views.home),
       path('lotto/',views.lotto),
   ]
   ```

2. views.py

   ```python
   def lotto(request):
       import random
       num = sorted(random.sample(range(1,46),6))
       context = {
           'lotto': num,
       }
       return render(request, 'lotto.html', context)
   ```

3. lotto.html

   ```html
   <body>
     <h3>로또 번호 추천 서비스</h3>
     {{lotto}}
   </body>
   ```

   



`ctrl + p` 를 누르고 찾고 싶은 파일 이름을 적으면, 뒤적뒤적 할 필요 없이 바로 갈 수 있다.



조건을 위해 if도 쓸 수 있드아ㅏ!!!

```html
<h3>DTL 조건문</h3>
{% if True %}
<p>이건 참일 때,</p>
{{ number }}
{% endif %}
```

```html
<h3>DTL 조건문</h3>
{% if False %}
<p>이건 0보다 커</p>
{% endif %}
```



로또 번호를 다르게 줄 수 있는 방법을 고안해보자

1~10:  노

11~20: 빨

21~30: 파

30~40: 회

40~45:

```html
<style>
  .numbers {
    margin-left: 20px;
    width:50px;
    height:50px;
    border-radius: 50%;
    background-color: cornflowerblue;
    text-align:center;
    line-height: 50px;
    color: rgb(243, 237, 237);
    display: inline-block;
  }
</style>
</head>
<body>
  <h1>로또 번호 추천 서비스</h1>
  <p>[</p>
  {% for i in lotto %}
  {% if i > 40$}
  <p class="numbers">{{i}}</p>
  {% elif i > 30 %}

  {$ elif i > 20 $}

  {% elif i > 10 %}

  {$ else %}

  {% endif %}
  {% endfor %}
  <p>]</p>
</body>
</html>
```



### DTL



- 데이터를 불러왔는데 없는 경우?

```html
<h2>데이터가 없을 때, </h2>
{% for movie in empty_data %}
<p> {{ movie }}</p>
{% empty %}
<p>영화 데이터가 없습니다.</p>
{% endfor %}
```



- counter는 어떻게?

```html
<h2>데이터가 없을 때, </h2>
{% for movie in empty_data %}
	<p> {{ forloop.counter }}: {{ movie }}</p>
{% empty %}
	<p>영화 데이터가 없습니다.</p>
{% endfor %}
```



- 이중 for문

```python
<h2>이중 for문은?</h2>
{% for array in matrix %}
{% for num in array %}
<p>{{ num }}</p>
{% endfor %}
{% endfor %}
```



템플릿을 상속해서 쓸 수 있다.

전체적인 껍질을 만들고 재사용하는 것



- helper or filter
  - builtin filter

fake text는 어떻게 넣지?

lorem ipsum

DTL은 그냥 바로 지원

lorem은 builtin-tag: 우리는 그냥 helper라고 하자

```html
<h2>다양한 helper or filter</h2>
<p>{% lorem %}</p>

<h2>다양한 helper or filter</h2>
<p>{% lorem 3 p random %}</p>
```

https://docs.djangoproject.com/en/2.2/ref/templates/builtins/



- filter

  - 필터로 정제해서 데이터를 뽑으려 할 때
  - 많이 쓰는 게 length

  ```html
  <h3>filter</h3>
  {% for movie in empty_data %}
   {{ movie| length}}
  {% endfor %}
  ```

  ```html
  <h3>filter</h3>
  {% for movie in empty_data %}
   {{ movie| length}}
   {{ movie| truncatechars:5}}
  {% endfor %}
  ```

  

  - int, 숫자로 가능	

  ```html
  <h4>int</h4>
  {{ number|add:10 }}
  <!-- 그러나 이런 건 좋지 않은 컨벤션. 자료 처리는 서버에서 해주고 넘겨야 한다. -->
  ```



DTL은 파이썬이 아니다. 다만 파이썬이랑 비슷할 뿐. html은 보여주는 것으로 끝내라

  - datetime

    <h4>datetime</h4>
{% now 'Y M D' %}



그런데 시간이 이상하다?

```html
<h4>datetime</h4>
{% now 'Y M D' %}
{% now 'h시 i분 a' %}
```

settings.py에서 

```python
TIME_ZONE = 'UTC'
이걸 다음과 같이 바꿔준다.
TIME_ZONE = 'Asia/Seoul'
```





### 가변적으로 들어오는 정보를 처리하자

```python
path('cube/<num>/', views.cube),
그러나 이건 str이기 때문에 int로 바꿔준다
path('cube/<int:num>/', views.cube),
```

```python
def cube(request, num):
    result= num*num*num
    context = {
        'result': result,
    }
    return render(request, 'cube.html',context)
```

```html
<body>
  <h1>cube 결과</h1>
  <p>{{ result }}</p>
</body>
```



- form을 활용해서 만들어보자

```html
<form action="/match/" method="GET">
  당신의 이름: <input type="text" name="me">
  그분의 이름: <input type="text" name="you">
  <button type='submit'>제출</button>
</form>

이렇게만 하면 page를 찾을 수 없다는 에러가 뜬다.
```



https://docs.djangoproject.com/en/2.2/ref/request-response/

```html
<body>
  <h1> {{ me }} 님과 {{ you }} 님의 궁합은 {{ goonghap }} % 입니다. </h1>
  <p>{{ path }}</p>
  <p>{{ test }}</p>
</body>
```

```python
def match(request):
    import random
    goonghap = random.randint(50,100)
    print(request)
    me = request.GET.get('me')
    you = request.GET.get('you')
    path = request.path_info
    test = request.get_host()

    context = {
        'goonghap': goonghap,
        'me': me,
        'you': you,
        'path': path,
        'test': test,
    }
    return render(request, 'match.html',context)
```



POST를 보낼 땐 csrf 토큰을 이용해서 요청을 검증한다. 처음에 요청을 보낼 때의 요청과 최종 도착한 토큰이 다를 경우 데이터 처리를 거부한다.

```python
def match(request):
    import random
    goonghap = random.randint(50,100)
    print(request)
    me = request.POST.get('me')
    you = request.POST.get('you')
    path = request.path_info
    test = request.get_host()

    context = {
        'goonghap': goonghap,
        'me': me,
        'you': you,
        'path': path,
        'test': test,
    }
    return render(request, 'match.html',context)
```

```html
<form action="/match/" method="POST">
  {% csrf_token%}
  당신의 이름: <input type="text" name="me">
  그분의 이름: <input type="text" name="you">
  <button type='submit'>제출</button>
</form>
```

