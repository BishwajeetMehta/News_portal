from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    gender =models.CharField(max_length=10,null=True)
    phone = models.CharField(max_length=50,blank=True,null=True)
    image = models.ImageField (null=True)


    def __str__(self):
        return self.first_name