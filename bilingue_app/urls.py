from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup', views.signup, name='signup'),
    path('vocabulary/', views.vocabulary_index, name='vocabulary'),
    path('word/create/', views.WordCreate.as_view(), name='word_create'),
    path('palabra/create/', views.PalabraCreate.as_view(), name='palabra_create'),
    path('media/create/', views.MediaCreate.as_view(), name='media_create'),
]