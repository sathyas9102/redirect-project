from distutils.command.upload import upload
from tokenize import Intnumber
from django.db import models


# Create your models here.

class Milk(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    liter=models.IntegerField()
    
class register(models.Model):
    username=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    password1=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)
    
    def _str_(self):
        return self.title