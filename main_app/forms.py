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

    # select_playlist = forms.ChoiceField(choices=[CHOICES], required=True)()
