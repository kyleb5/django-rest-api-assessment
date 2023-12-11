from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    bio = models.TextField()
