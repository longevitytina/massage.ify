from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Followings(models.Model):
    from_user = models.ForeignKey(
        User, related_name='follower', on_delete=models.CASCADE)

    to_user = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
