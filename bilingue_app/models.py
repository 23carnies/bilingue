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
    avatar = models.FileField(blank=True)
    bio = models.TextField(
        max_length=300,
        blank=True)
    native_language = models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse('home')

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
    year = models.CharField(max_length=4, blank=True, 
        help_text= "2005")
    picture = models.CharField(max_length=250, blank=True,
        help_text= "http link")
    media_type = models.CharField(
        max_length=1,
        choices=MEDIA_TYPES,
        default=MEDIA_TYPES[0][0]
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} is a {self.get_media_type_display()}"
    def get_absolute_url(self):
        return reverse('media')

class Chiste(models.Model):
    título = models.CharField(max_length=100,
        help_text= "Title")
    configuración = models.CharField(
        max_length=500,
        blank=True,
        help_text= "Setup in Spanish"
    )
    remate = models.CharField(
        max_length=200,
        blank=True,
        help_text= "Punchline in Spanish"
    )
    set_up = models.CharField(
        max_length=500,
        blank=True
    )
    punchline = models.CharField(
        max_length=200,
        blank=True
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    def __str__(self):
        return self.título  
    def get_absolute_url(self):
        return reverse('chistes')


