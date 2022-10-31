from distutils import extension
from email.policy import default
from operator import imod
from django.db import models
from datetime import datetime
from time import timezone
from artists.models import Artist
from model_utils.models import TimeStampedModel
# Create your models here.


class Album(TimeStampedModel):

    artist_fk = models.ForeignKey(Artist, on_delete=models.CASCADE)

    album_name = models.CharField(
        max_length=200, default="New Album", verbose_name="New Album")

    release_time = models.DateTimeField('publish time')

    album_cost = models.DecimalField(max_digits=20, decimal_places=2)

    album_is_approved = models.BooleanField(
        default=True, help_text=" Approve the album if its name is not explicit")

    def __str__(self):
        return "name = " + self.album_name + " Artist = " + self.artist_fk.stage_name

    def time_zone(self):
        return self.release_Time <= timezone.now()

    def time_zone(self):
        return self.release_Time <= timezone.now() - datetime.timedelta(days=1)
