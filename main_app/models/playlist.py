from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
from .technique import Technique


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    techniques = models.ManyToManyField(
        'Technique', through="PlaylistTechnique")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index", kwargs={"pk": self.id})
