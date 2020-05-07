from django import forms
from .models import Playlist, PlaylistTechnique


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ('name',)


# class TechniqueForm(forms.ModelForm):
#     class Meta:
#         model = PlaylistTechnique
#         fields = ('techniques', 'order')
