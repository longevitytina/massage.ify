from django.db import models


class Following(models.Model):
    from_user = models.ForeignKey(
        "Profile", related_name='follower', on_delete=models.CASCADE)

    to_user = models.ForeignKey(
        "Profile", related_name='following', on_delete=models.CASCADE)
