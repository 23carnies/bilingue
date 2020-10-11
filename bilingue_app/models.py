from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    avatar = models.CharField(
        max_length=300,
        blank=True)
    bio = models.TextField(
        max_length=500,
        blank=True)
    native_language = models.TextField(max_length=100)

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
    def get_absolute_url(self):
        return reverse('vocabulary')
