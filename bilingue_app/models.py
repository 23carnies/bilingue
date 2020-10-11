from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class User(AbstractUser):
    avatar = models.CharField(max_length=200)
    bio = models.TextField(max_length=500)
    language = models.TextField(max_length=100)

class Word(models.Model):
    english = models.CharField(max_length=100)
    spanish = models.CharField(
        max_length=100,
        blank=True
        )
    cognates = models.CharField(
        max_length=200,
        blank=True
        )
    antonyms = models.CharField(
        max_length=200,
        blank=True
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.english
    def get_absolute_url(self):
        return reverse('vocabulary')

class Palabra(models.Model):
    español = models.CharField(max_length=100)
    inglés = models.CharField(
        max_length=100,
        blank=True
        )
    cognadas = models.CharField(
        max_length=200,
        blank=True
        )
    antónimos = models.CharField(
        max_length=200,
        blank=True
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.español  
    def get_absolute_url(self):
        return reverse('vocabulary')
