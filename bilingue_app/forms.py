from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'native_language')

class UserUpdateForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'native_language')

        