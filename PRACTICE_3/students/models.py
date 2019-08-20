from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    birthday = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)