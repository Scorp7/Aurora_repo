from django.db import models

# Create your models here.
class UserData(models.Model):
    gender = (("1","Male"),("2","Female"))
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    email = models.EmailField(max_length=70)
    gender = models.CharField(max_length=50, choices=gender)
    password = models.CharField(max_length=70)
    
class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)