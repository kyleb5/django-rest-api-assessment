from django.db import models
from .artist import Artist


class Song(models.Model):
    title = models.CharField(max_length=25)
    album = models.CharField(max_length=25)
    length = models.IntegerField()
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE, default=1)
