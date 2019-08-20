from django.db import models

# Create your models here.
class Post(models.Model):
    # id title content created_at updated_at img_url 작성자 태그 조회수 추천 댓글 좋아요
    # 태깅이 좀 까다롭다
    # id는 우리가 건드릴 필요 없이 알아서 만들어줌
    title = models.CharField(max_length=100)
    # 이메일, 유저 아이디 등은 작은 규모이기 때문에 charfield가 적당하다
    content = models.TextField()
    img_url = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True) # 만들어졌을 때
    updated_at = models.DateTimeField(auto_now=True) # 들어왔을 때의 시간을 기록
    