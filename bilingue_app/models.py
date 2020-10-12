from django.db import models
from django.contrib.auth import get_user_model
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
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=250)
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
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.english

    def get_absolute_url(self):
        return reverse('word')

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
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)    
    def __str__(self):
        return self.español  
    def get_absolute_url(self):
        return reverse('palabra')

class Photo(models.Model):
    url = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for user_id: {self.user_id} @{self.url}"

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
    photos = models.ManyToManyField(Photo)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} is a {self.get_media_type_display()}"
    def get_absolute_url(self):
        return reverse('media')

class Chiste(models.Model):
    título = models.CharField(max_length=100)
    foto = models.CharField(
        max_length=200,
        blank=True
    )
    configuración = models.CharField(
        max_length=500,
        blank=True
    )
    remate = models.CharField(
        max_length=200,
        blank=True
    )
    photos = models.ManyToManyField(Photo)
    def __str__(self):
        return self.título  
    def get_absolute_url(self):
        return reverse('chistes')


