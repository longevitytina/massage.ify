from django import forms
from .models import PlaylistTechnique


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = PlaylistTechnique
        fields = ('technique', 'duration', 'order')
