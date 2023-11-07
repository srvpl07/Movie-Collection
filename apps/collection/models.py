from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser ,Group, Permission

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set')
    
class Genere(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Movies(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    uuid = models.CharField(primary_key=True, max_length=40)
    genere = models.ManyToManyField(Genere)

    def __str__(self):
        return self.title
    
class Collection(models.Model):
    uuid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movies)

    def __str__(self):
        return self.title

class RequestCounter(models.Model):
    count = models.IntegerField(default=0)
