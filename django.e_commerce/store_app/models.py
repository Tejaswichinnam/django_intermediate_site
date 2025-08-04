from django.db import models
from datetime import datetime

# Create your models here.

class Useradd(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=300)
    password=models.CharField(max_length=50)


    def __str__(self):
        return self.username
    
class Contact(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    mob_num=models.IntegerField()
    city=models.TextField()
    feedback=models.TextField()
    created_at=models.DateTimeField(default=datetime.now)
    is_resolved=models.BooleanField(default=False)


    def __str__(self):
        return self.firstname
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=50)
    image = models.URLField()
    link = models.URLField()

    def __str__(self):
        return self.title
