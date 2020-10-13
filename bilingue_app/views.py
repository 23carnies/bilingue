from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Word, Palabra, Media, Chiste, Photo
from .forms import SignupForm, UserUpdateForm
import uuid
import boto3


S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = '23carnies'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = SignupForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class User_Detail(LoginRequiredMixin, DetailView):
    model = get_user_model()

@login_required
def vocabulary_index(request):
    words = Word.objects.filter(user=request.user)
    palabras = Palabra.objects.filter(user=request.user)
    return render(request, 'vocabulary.html', 
        { 'palabras': palabras, 'words': words }
    )

@login_required
def media_index(request):
    medias = Media.objects.all()
    return render(request, 'media.html', {'medias': medias})

@login_required
def chiste_index(request):
    chistes = Chiste.objects.all()
    return render(request, 'chistes.html', {'chistes': chistes})

class WordCreate(LoginRequiredMixin, CreateView):
    model = Word
    fields = ['english', 'spanish', 'cognates', 'antonyms']
    success_url = '/vocabulary/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PalabraCreate(LoginRequiredMixin, CreateView):
    model = Palabra
    fields = ['español', 'inglés', 'cognadas', 'antónimos']
    success_url = '/vocabulary/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MediaCreate(LoginRequiredMixin, CreateView):
    model = Media
    fields = ['name', 'year', 'picture', 'media_type']
    success_url = '/media/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ChisteCreate(LoginRequiredMixin, CreateView):
    model = Chiste
    fields = ['título', 'foto', 'configuración', 'remate']
    success_url = '/chistes/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class WordUpdate(LoginRequiredMixin, UpdateView):
    model = Word
    fields = ['english', 'spanish', 'cognates', 'antonyms']
    success_url = '/vocabulary/'

class PalabraUpdate(LoginRequiredMixin, UpdateView):
    model = Palabra
    fields = ['español', 'inglés', 'cognadas', 'antónimos']
    success_url = '/vocabulary/'

class MediaUpdate(LoginRequiredMixin, UpdateView):
    model = Media
    fields = ['name', 'year', 'picture', 'media_type']
    success_url = '/media/'

class ChisteUpdate(LoginRequiredMixin, UpdateView):
    model = Chiste
    fields = ['título', 'foto', 'configuración', 'remate']
    success_url = '/chistes/'

class UserUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'registration/user_change_form.html'
    form_class = UserUpdateForm
    model = get_user_model()
    def get_object(self, queryset=None):
        return self.request.user


class WordDelete(LoginRequiredMixin, DeleteView):
    model = Word
    success_url = '/vocabulary/'

class PalabraDelete(LoginRequiredMixin, DeleteView):
    model = Palabra
    success_url = '/vocabulary/' 

class MediaDelete(LoginRequiredMixin, DeleteView):
    model = Media
    success_url = '/media/'

class ChisteDelete(LoginRequiredMixin, DeleteView):
    model = Chiste
    success_url = '/chistes/'

class UserDelete(LoginRequiredMixin, DeleteView):
    model = get_user_model()
    success_url = '/about/'

def user_photo(request, user_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}/{BUCKET}/{key}"
            user = get_user_model().objects.get(id=user_id)
            user.avatar = url
            user.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('/', user_id=user_id)

def media_photo(request, media_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}/{BUCKET}/{key}"
            media = Media.objects.get(id=media_id)
            media.picture = url
            media.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('/media/', media_id=media_id)
