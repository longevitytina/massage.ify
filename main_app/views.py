from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def techniques_list(request):
    return render(request, 'techniques/technique_index.html')


def profile(request):
    return render(request, 'profile.html')
