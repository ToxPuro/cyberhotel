from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hotel(models.Model):
    name=models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    cost = models.IntegerField(default=100)

class Receipt(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE) 

class Card(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    cardnumber=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class Comment(models.Model):
    content=models.CharField(max_length=100)

