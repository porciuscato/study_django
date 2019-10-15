# 10월 14일

모던 프레임워크에서 가장 중요한 것! DRY. 반복되지 않는 것

-> 코드의 재사용성을 높일 것



Form -> Model Form

Auth 인증과 권한까지..

Class based view. 장고만 사용하는 것들



M : N 디비 구축

Validation

-> 이후 Deploy



2010년도가 넘어가면서 (예전에는 클릭 이후 페이지가 변화. 그런데 모바일 페이지가 계속 로드되는 것이 부담. 클라이언트 사이드에서 계속 랜더링이 되도록 만드는 것이 만들어짐 -> 자바스크립트의 시대. (이전에는 Adobo))

=> google이 자바스크립트 만으로(어도비를 사용하지 않고) google maps를 구현

아이폰이 나오면서 어도비를 포함하지 않고 지금은 완전 자바스크립트 세상



그러나 자바스크립트는 그 자체로 너무 유지보수가 어려움

그래서 framework가 나옴. (Ember, Backbone 등 프레임 워크들이 있었으나 이들은 너무 헤비했음. 결국 이들은 사장되기 시작.) 이제는 facebook이 React를 만듦. 주로 프레임워크 등은 회사에서 만들어진 것들이 많음

구글이 만든 angular. 

React, Angular, Vue -> 이게 가장 많이 쓰임

스택오버플로우에 검색되는 것이  사용량

Vue가 2위로 올랐는데 심플함.

React는 가장 많이 쓰지만 초반에 배우기가 너무 어려움. 그래서 vue를 배움

`TDD` test driven development: 이거 할 수 있는 사람 우대



모델과 모델폼에 대해...

Model and Model Form



`어떤 원칙에 입각해서 DRY하게 짜는 것이 개발인가?`





자바스크립트 프레임워크...

웹 react는 그대로 사용해서 모바일 앱으로 만들 수 있을 정도로 좋음. 

React native





장고 복습

```python
USE_I18N = True
# 번역을 해주는 친구
```



프로젝트 시작할 땐 항상 모델을 만들고 시작하는 것이 좋다.



validation의 기본을 배우고 test코드를 짜는 것

TDD는? test가 중간에 있는 D가 중요... `Driven`이 개발 전체를 주도한다.

코드가 에러 나는지 검증을 하는 것. 테스트 코드를 만드는 것.

TDD에서는 이미 테스트케이스가 있는 상태에서 우리의 코드를 수정해나가는 것

구현해낼 것들이 커버할 것들을 미리 다아아 만들어 놓는 것. (마치 알고리즘 문제를 테스트케이스를 줄이는 것)

이것들을 초록불로 바꾸는 것이 개발!

테스트가 개발을 주도한다!

테스트를 먼저 짜고 개발을 후에 한다.



TDD를 안 짜고 가면 앱이 커졌을 때 앱이 터질 수도 있다.

앱은 하나가 아니라 다른 앱들과 연동되어있기 때문

코드를 견고하게 짜지 않으면 나중에 터짐....

```
실리콘밸리 에어비앤비
이 분의 조언
```

 depth를 파기보다 먼저 넓게 많이 알아야 한다.







admin 빌딩해서 가보자



속성들을 디스플레이 하기 위한 방법?



사용자가 보는 것 하나, 관리자가 보는 것 하나(게임사는 오히려 관리자 페이지가 더 빡세다)



브라우저는?
우리를 대신해서 서버에 요청을 보내주고 http 파일을 바꿔주는 것

요청을 보내고 응답을 보여주는 것

html이 조작하는 것

서버에 요청을 보내지도 않았는데 반응을 한다? 그러면 거의 자바스크립트



```
ctl + shift + j 
하고
print() 하면 이게 뜸!!
```



crud 버전의

`restfull api`

동사를 없애버렸다.



요새는 REST API. 규칙을 지키는 API들

django rest framework



detail view는



url을 넘길 때 

` http://localhost:8000/admin/login/?next=/admin/ `

next: 나중에 어디로 가라고 알려줌. 혹은 이 사람이 어디를 눌러서 들어왔는지도 알려줌

텀블러 페이지를 누르더라도 url에서 어디를 누르고 왔는지 다 확인이 가능하다.

훨씬 data driven 하기 좋다. -> 이것이 개발자의 소관으로 넘어오고 있다.

버튼으로 이 사람들을 어떻게 tracking 하는지 보여줌 -> 대부분 자바스크립트



`GraphQL` : 만들어진지 5년 밖에 안 된...

github은 rest와 graphQL 둘 다 할 수 있다.







module화가 되지 않을까?

1단계 업그레이드가 form

2단계가 model form



사용자는? 또라이다.

어떤 짓을 할지 모른다... validation을 검사해서 입력을 통제해야 한다.



유효성 검사





코드셋을 잘 만들어놓으면 다른 사람이 가져와서 쓸 수 있다.



장고 bootstrap4

django bootstrap4



```html
{% load bootstrap4 %}
{% bootstrap_css %}
{% bootstrap_javascript jquery='full' %}
```

장고로 bootstarp을 사용하기



form은 2가지 다 막고 있음



auth... 상용 auth는 본인이 직접 짜면 안 됨

암호화가 덜 된 상태거나, 혹은 간단한 해시 알고리즘을 썼다가 정부 사람들 오면 걸릴 수 있음(개인정보에 대한 철저한 관리)



바닥부터 잘 안 짬

auth 서비스를 그냥 씀

로그인 모듈을 다른 회사에 넘겨버림.

-> 코드가 모듈화가 잘 되어있으면 붙여넣기가 편리함



가장 중요한 건 DRY





# 10월 15일

IPython embed function

python manage.py shell_plus



`embed()` : 일종의  프리즈. 날아가는 정보를 멈춰놓고 날아가는 데이터를 볼 수 있음

를 추가하면

runserver 도중에 쉘이 켜진다.

IPython은 장고랑 상관없음.



새글쓰기를 하니 서버가 멈추고 shell_plus가 떴음

form을 치면 어떤 객체가 튀어나옴

request.POST



cleaned_data : 유효성 검사가 끝난 것

어디서 데이터가 안 넘어오는지 확인할 수 있음

embed()라는 함수를 사용하면 됨



form.as_p()

form.as_table()

form.as_ul()



http는 무상태성이다?

http는 





comment 생성 & 삭제

-- POST /articles/:id/comments

-- POST /articles/:id/comments_delete/:c_id

-- ModelForm 활용