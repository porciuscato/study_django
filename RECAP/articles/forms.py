from django import forms
from .models import Article, Comment


# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=20,
#         label='제목',
#         help_text='제목은 20글자 이내로 써주세요',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control my-title',
#                 'placeholder': '제목을 입력해주세요',
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class':'form-control my-content',
#                 'placeholder': '내용을 입력해주세요',
#                 'rows': 5,
#             }
#         )
#     )

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # 특정 필드 선택
        # fields = '__all__'
        # all은 모든 필드들을 다 가져오게 됨
        fields = ('title', 'content',)
        # widgets = {
        #     # '필드(칼럼))': Form 속성,
        #     'title': forms.TextInput(
        #         attrs={
        #             'placeholder': '제목을 입력해주세요',
        #             'class': 'form-control title-class',
        #             'id': 'title',
        #         })
        #     }

    title = forms.CharField(
        max_length=20,
        label='제목',
        help_text='제목은 20글자 이내로 써주세요',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control my-title',
                'placeholder': '제목을 입력해주세요',
            }
        )
    )
    
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class':'form-control my-content',
                'placeholder': '내용을 입력해주세요',
                'rows': 5,
            }
        )
    )
    
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)