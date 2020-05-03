from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
from .technique import Technique


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index", kwargs={"pk": self.id})


class JoinPlaylist(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE)
    time = models.TimeField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
