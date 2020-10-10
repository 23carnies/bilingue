from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    avatar = models.CharField(max_length=200)
    bio = models.TextField(max_length=500)
    language = models.TextField(max_length=100)

class Vocabulary(models.Model):
    english = models.CharField(
        max_length=100,
        blank=True
        )
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

