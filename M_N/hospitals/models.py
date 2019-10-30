from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()

# 중개모델
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)