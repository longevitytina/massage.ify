from django.db import models


class PlaylistTechnique(models.Model):
    playlist = models.ForeignKey("Playlist", on_delete=models.CASCADE)
    technique = models.ForeignKey("Technique", on_delete=models.CASCADE)
    time = models.TimeField()
    order = models.PositiveIntegerField(default=0)
