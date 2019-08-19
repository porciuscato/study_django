from django.db import models

# Create your models here.
class Article(models.Model):
    # 데이터베이스는 메타데이터인 스키마를 가지고 있다. 이걸 정의해주는 것
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 자동으로 현재 시간을 넣는 것
    image_url = models.TextField()

    def __str__(self):
        return f'{self.id} : {self.title}'
