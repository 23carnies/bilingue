from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=100, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required*')
    first_name = forms.CharField(max_length=100, required=True, help_text='Required*')
    avatar = forms.CharField(max_length=300, required=False, help_text='Optional')    
    bio = forms.CharField(max_length=500, required=False, help_text='Optional')
    native_language = forms.CharField(max_length=100, required=True, help_text='Required*')

    class Meta:
        model = User
        fields = ('username','first_name', 'email', 'avatar', 'native_language')