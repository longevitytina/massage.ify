from django.db import models
from django.urls import reverse


class Technique(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, default="To be added..")
    instructions = models.CharField(max_length=1000)
    image_url = models.URLField()
    video_url = models.URLField()
    author = models.ForeignKey(
        'Profile', default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index", kwargs={"technique_id": self.id})
