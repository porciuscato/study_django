from django import forms
from .models import Article, Comment


# Form / ModelForm : 1 .Date Validation 2. HTML 생성

class ArticleForm(forms.ModelForm):
    # 들어온 자료가 타당한지 검증하는 것
    # 1. HTML을 어떻게 만들 것인가
    # 2. 검증을 한다면, 어떤 조건으로 검증할 것인가
    # 3. 만약 아무것도 쓰지 않는다면 
        # 1. ModelForm은 Model을 알고 있기 때문에.
        # 2. 각 Model을 읽고, 알아서 HTML + 검증을 시행
        # + python manage.py dbshell 을 입력하고 .schema를 하면 DB의 칼럼을 볼 수 있음
    title = forms.CharField(min_length=2, max_length=200)
    # content에 대하여 어떤 검증/HTML 관련해서 적지 않았다 -> 알아서 models.Article의 content 항목을 보고 할 일을 한다.
    class Meta:
        model = Article
        # fields에 적힌 column은 검증하겠다는 의미
        fields = ('title', 'content',)
        # 만약 이렇게 쓴다면?
        # fields = (, 'content') ??

class CommentForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200)

    class Meta:
        model = Comment
        fields = ('content',)