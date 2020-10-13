from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup', views.signup, name='signup'),
    path('vocabulary/', views.vocabulary_index, name='vocabulary'),
    path('word/create/', views.WordCreate.as_view(), name='word_create'),
    path('words/<int:pk>/update/', views.WordUpdate.as_view(), name='words_update'),
    path('words/<int:pk>/delete/', views.WordDelete.as_view(), name='words_delete'),
    path('palabra/create/', views.PalabraCreate.as_view(), name='palabra_create'),
    path('palabras/<int:pk>/update/', views.PalabraUpdate.as_view(), name='palabras_update'),
    path('palabras/<int:pk>/delete/', views.PalabraDelete.as_view(), name='palabras_delete'),
    path('media/create/', views.MediaCreate.as_view(), name='media_create'),
    path('media/', views.media_index, name='media_index'),
    path('media/<int:pk>/update/', views.MediaUpdate.as_view(), name='media_update'),
    path('media/<int:pk>/delete/', views.MediaDelete.as_view(), name='media_delete'),
    path('chistes/create/', views.ChisteCreate.as_view(), name='chistes_create'),
    path('chistes/', views.chiste_index, name='chistes_index'),
    path('chistes/<int:pk>/update/', views.ChisteUpdate.as_view(), name='chistes_update'),
    path('chistes/<int:pk>/delete/', views.ChisteDelete.as_view(), name='chistes_delete'),
    path('accounts/<int:pk>/', views.User_Detail.as_view(), name='user_detail'),
    path('accounts/<int:pk>/update', views.UserUpdate.as_view(), name='user_update'),
    path('accounts/<int:pk>/delete', views.UserDelete.as_view(), name='user_delete'),
]