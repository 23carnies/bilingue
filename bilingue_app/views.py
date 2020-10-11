from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User, Word, Palabra

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


class WordCreate(LoginRequiredMixin, CreateView):
    model = Word
    fields = ['english', 'spanish', 'cognates', 'antonyms']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PalabraCreate(LoginRequiredMixin, CreateView):
    model = Palabra
    fields = ['español', 'inglés', 'cognadas', 'antónimos']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def vocabulary_index(request):
    words = Word.objects.filter(user=request.user)
    palabras = Palabra.objects.filter(user=request.user)
    return render(request, 'vocabulary.html', 
        { 'palabras': palabras, 'words': words }
    )