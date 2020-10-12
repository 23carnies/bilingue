from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User, Word, Palabra, Media, Chiste, Photo
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

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
    fields = ['name', 'year', 'picture', 'media_type', 'is_streaming']
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

class ChisteUpdate(LoginRequiredMixin, UpdateView):
    model = Chiste
    fields = ['título', 'foto', 'configuración', 'remate']
    success_url = '/chistes/'

class WordDelete(LoginRequiredMixin, DeleteView):
    model = Word
    success_url = '/vocabulary/'

class PalabraDelete(LoginRequiredMixin, DeleteView):
    model = Palabra
    success_url = '/vocabulary/'

class ChisteDelete(LoginRequiredMixin, DeleteView):
    model = Chiste
    success_url = '/chistes/'

@login_required
def add_photo(request, cat_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, cat_id=cat_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', cat_id=cat_id)
    #I have questions about everything below 121