from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# manage.py loaddata techniques <fixturename>


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index", kwargs={"pk": self.id})


class Technique(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, default="To be added..")
    instructions = models.CharField(max_length=1000)
    image_url = models.URLField()
    video_url = models.URLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index", kwargs={"pk": self.id})

# Join tables------------------------


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Technique)


# class Favorites(models.Model):
#     # user = models.ManyToManyField(User)
#     technique = models.ManyToManyField(Technique)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# when a user follows another user


class Followings(models.Model):
    from_user = models.ForeignKey(
        User, related_name='follower', on_delete=models.CASCADE)

    to_user = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE)

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


# adds a technique to user's favorites index
