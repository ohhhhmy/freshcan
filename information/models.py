from django.db import models
from django.conf import settings

# Create your models here.
class Vegetable(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField(max_length = 300)

    def __str__(self):
        return self.title

class Meat(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField(max_length = 300)

    def __str__(self):
        return self.title


class Grain(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField(max_length = 300)

    def __str__(self):
        return self.title
    

class Fruit(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField(max_length = 300)

    def __str__(self):
        return self.title

class Seafood(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField(max_length = 300)

    def __str__(self):
        return self.title

class Information(models.Model):
    name = models.CharField(max_length=300)
    body = models.TextField()
    TITLE = (('01','곡물/견과류'), ('02', '채소'), ('03', '과일'), ('04', '해산물'), ('05', '육류/기타'))

    title = models.CharField(max_length=2, choices=TITLE)

    update_date = models.DateTimeField(auto_now=True)

    def ___str___(self):
        return self.title