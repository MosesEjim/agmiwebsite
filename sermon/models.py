from django.db import models

# Create your models here.
class Sermon(models.Model):
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    date = models.DateField()
    photo = models.FileField()
    file = models.FileField()

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=100)
    aboutEvent = models.CharField(max_length=1000)
    photo = models.FileField()

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=3000)
    photo = models.FileField()
    author = models.CharField(max_length= 30)
    date = models.DateField()

    def __str__(self):
        return self.title