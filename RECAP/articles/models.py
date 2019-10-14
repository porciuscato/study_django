from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-pk',)
        # objects.all 하면 뒤집어져서 나옴
    
    # method도 추가예정
    def get_absolute_url(self):
        # '어디로 갈지가 첫 번째 인자', '인자'
        return reverse('articles:detail', kwargs={'pk':self.pk})
        # 자기가 가진 pk로 url을 생성
        # 객체를 넘기더라도, reverse함수의 결과물인 url이 나오기 때문에 redirect가 된다.

        