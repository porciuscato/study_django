from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    img_url = models.TextField()