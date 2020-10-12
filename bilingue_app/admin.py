from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Word, Palabra, Media, Chiste

# Register your models here.
admin.site.register(get_user_model())
admin.site.register(Word)
admin.site.register(Palabra)
admin.site.register(Media)
admin.site.register(Chiste)