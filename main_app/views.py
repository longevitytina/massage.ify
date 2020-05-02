from django.shortcuts import render
from .models import *


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
