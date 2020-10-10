from django.contrib import admin
from .models import User, Word, Palabra

# Register your models here.
admin.site.register(User)
admin.site.register(Word)
admin.site.register(Palabra)
