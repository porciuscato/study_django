from django.db import models


# models.Model을 상속받는 Class 에서 class 멤버변수는 테이블의 컬럼이 됨
class Article(models.Model):
    # id(pk)는 자동생성
    # id = INTEGER AUTO INCREMENT UNIQUE
    title = models.CharField(max_length=200) # CREATE TABLE board_article(title=VARCHAR)
    content = models.TextField()
    # 처음 저장 될 때의 시간만 저장
    created_at = models.DateTimeField(auto_now_add=True)
    # 저장(.save())될 때의 시간을 저장
    updated_at = models.DateTimeField(auto_now=True)

    # 그냥 ordering으로 쓰면 칼럼이 되기 때문에 Meta를 정의하는 것
    class Meta:
        # 여러 옵션을 주면 앞에서부터 정렬
        ordering = ('-created_at',)

class Comment(models.Model):
    # id = INTEGER AUTO INCREMENT UNIQUE
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
