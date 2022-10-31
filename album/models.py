from distutils import extension
from email.policy import default
from operator import imod
from django.db import models
from datetime import datetime
from time import timezone
from artists.models import Artist
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from django.core.validators import FileExtensionValidator
from imagekit.processors import ResizeToFill
from django.core.exceptions import ValidationError
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


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True,
                            help_text="if no name is provided, the song's name defaults to the album name")
    img = models.ImageField(blank=False, upload_to="image")
    thumbnail = ImageSpecField(source='img',
                               processors=[ResizeToFill(100, 50)],
                               format='JPEG',
                               options={'quality': 60})
    audio = models.FileField(upload_to="music", blank=False, validators=[
                             FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])

    def save(self, *args, **kwargs):
        if self.name == "":
            self.name = self.album.name
        super(Song, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if (self.album.song_set.all().count() > 1):
            super(Song, self).delete(*args, **kwargs)
        else:
            raise ValidationError("album has only 1 song , can't be deleted")
