from operator import mod
from re import T
from django.db import models


# Create your models here.




class Announcement(models.Model):
    title=models.CharField(max_length=50)
    host = models.CharField(max_length=50)
    host_title=models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.title


class Lesson(models.Model):
    name=models.CharField(max_length=50)
    tutor = models.CharField(max_length=50)
    image = models.ImageField(null=True, default="avatar.svg")
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Commission(models.Model):
    name=models.CharField(max_length=100)
    chair = models.CharField(max_length=100)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class News(models.Model):
    title=models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    image = models.ImageField(default="avatar.svg")
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.title



class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default="avatar.svg")

    def __str__(self):
        return self.name



class User(models.Model):
    pass

