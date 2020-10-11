from django.contrib import admin
from .models import User, Word, Palabra, Media

# Register your models here.
admin.site.register(User)
admin.site.register(Word)
admin.site.register(Palabra)
admin.site.register(Media)