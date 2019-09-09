from django.db import models

# Create your models here.
class data(models.Model):
    title=models.CharField(max_length=100)
    author= models.CharField(max_length=50)
    publisher= models.CharField(max_length=50)
    introduction = models.TextField()
    
