from django.db import models

# Create your models here.
class Person(models.Model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    age= models.CharField(max_length=30)
class Employee(models.Model):
    username= models.CharField(max_length=30)
    password= models.CharField(max_length=30)
class Indibagallery(models.Model):
    title= models.CharField(max_length=50)
    body= models.CharField(max_length=50)
    image= models.ImageField()