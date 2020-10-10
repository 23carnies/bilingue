from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    avatar = models.CharField(max_length=200)
    bio = models.TextField(max_length=500)

class Vocabulary(models.Model):
    english = models.CharField(max_length=100)
    spanish = models.CharField(max_length=100)
    cognates = models.CharField(max_length=200)
    antonyms = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

