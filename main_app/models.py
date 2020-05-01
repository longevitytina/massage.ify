from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
#


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


def __str__(self):
    return self.name


def get_absolute_url(self):
    return reverse("index", kwargs={"pk": self.id})


class Technique(models.Model):
    name = models.CharField(max_length=100)
    instructions = models.CharField(max_length=500)
    image_url = models.URLField()
    video_url = models.URLField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index", kwargs={"pk": self.id})

# Join tables------------------------

# when a user follows another user


class Followings(models.Model):
    from_user = models.ForeignKey(
        User, related_name='follower', on_delete=models.CASCADE)

    to_user = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# adds a technique to user's favorites index


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    technique = models.ForeignKey(Technique, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# complete playlist with playlist_id, technique_ids, time(per technique), and order


class JoinPlaylist(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE)
    time = models.TimeField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
