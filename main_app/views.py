from django.shortcuts import render
from .models import *
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def techniques_list(request):
    techniques = Technique.objects.all()
    return render(request, 'techniques/technique_index.html', {'techniques': techniques})


def technique_detail(request, technique_id):
    technique = Technique.objects.get(id=technique_id)
    return render(request, 'techniques/technique_detail.html', {'technique': technique})


def profile(request):
    return render(request, 'profile.html')


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
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
