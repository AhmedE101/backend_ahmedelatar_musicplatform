from email.policy import default
from django.db import models
from datetime import datetime
from time import timezone
from artists.models import Artist
# Create your models here.


class Album(models.Model):

    artist_fk = models.ForeignKey(Artist, on_delete=models.CASCADE)

    album_name = models.CharField(
        max_length=200, default="New Album", verbose_name="New Album")

    creation_time = models.DateTimeField(
        'time created', unique=True, default=timezone)

    release_time = models.DateTimeField('publish time')

    album_cost = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return "name = " + self.album_name + "-->" + " Artist = " + self.artist_fk.stage_name
