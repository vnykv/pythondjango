from django.db import models

class users(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    age=models.CharField(max_length=20)
