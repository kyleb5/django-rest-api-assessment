from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField(default=3)
    bio = models.CharField(max_length=500)
