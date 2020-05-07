from django.db import models


class PlaylistTechnique(models.Model):
    playlist = models.ForeignKey("Playlist", on_delete=models.CASCADE)
    technique = models.ForeignKey("Technique", on_delete=models.DO_NOTHING)
    duration = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)
