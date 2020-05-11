from django import forms
from .models import Playlist, PlaylistTechnique


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ('name',)


class SelectPlaylistForm(forms.ModelForm):
    class Meta:
        model = PlaylistTechnique
        fields = ('playlist', 'duration', )


class ChangeTechniqueTime(forms.ModelForm):
    class Meta:
        model = PlaylistTechnique
        fields = ('duration',)


class OrderingForm(forms.Form):
    ordering = forms.CharField
