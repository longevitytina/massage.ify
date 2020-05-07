from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import *


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def techniques_list(request):
    if request.user.is_authenticated:
        techniques = Technique.objects.all()
        profile = request.user.profile
        context = {
            'profile': profile,
            'techniques': techniques
        }
        return render(request, 'techniques/technique_index.html', context)
    else:
        techniques = Technique.objects.all()
        return render(request, 'techniques/technique_index.html', {'techniques': techniques})


def technique_detail(request, technique_id):
    technique = Technique.objects.get(id=technique_id)
    return render(request, 'techniques/technique_detail.html', {'technique': technique})


@login_required
def profile(request):
    profile = request.user.profile

    user = request.user
    context = {
        'profile': profile,

        'user': user
    }
    return render(request, 'profile.html', context)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def assoc_technique(request, profile_id, technique_id):
    Profile.objects.get(id=profile_id).favorites.add(technique_id)

    technique = Technique.objects.get(id=technique_id)

    return redirect('techniques_list')


def new_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)

            playlist.user = request.user.profile
            playlist.save()
            return redirect('profile')

    else:
        form = PlaylistForm()
    context = {'form': form}
    return render(request, 'playlists/playlist_form.html', context)


def playlist_detail(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    techniques = playlist.techniques.all()
    context = {'playlist': playlist,
               'techniques': techniques}

    return render(request, 'playlists/playlist_detail.html', context)


def delete_favorite(request, technique_id):
    profile = request.user.profile
    technique = Technique.objects.get(id=technique_id)
    profile.favorites.remove(technique)

    return redirect('profile')


def delete_playlist(request, playlist_id):
    Playlist.objects.get(id=playlist_id).delete()
    print(playlist_id)
    return redirect('profile')
