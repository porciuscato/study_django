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