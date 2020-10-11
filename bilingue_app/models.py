from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

MEDIA_TYPES = (
    ('C', 'Cines'),
    ('L', 'Libros'),
    ('T', 'Programa de TV'),
    ('P', 'Podcasts'),
    ('M', 'Música')
)

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

class Media(models.Model):
    name = models.CharField(max_length=250)
    year = models.IntegerField(blank=True, null=True)
    picture = models.CharField(
        max_length=200,
        blank=True
        )
    media_type = models.CharField(
        max_length=1,
        choices=MEDIA_TYPES,
        default=MEDIA_TYPES[0][0]
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} \n {self.get_media_type_display()}"
    def get_absolute_url(self):
        return reverse('media')
