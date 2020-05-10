from django import forms
from .models import Playlist, PlaylistTechnique


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ('name',)


class SelectPlaylistForm(forms.ModelForm):
    class Meta:
        model = PlaylistTechnique
        fields = ('playlist', 'duration', 'order')


class ChangeTechniqueTime(forms.ModelForm):
    class Meta:
        model = PlaylistTechnique
        fields = ('duration', 'order')
