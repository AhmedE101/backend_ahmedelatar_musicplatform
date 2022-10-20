from datetime import datetime
from email.policy import default
from time import timezone
from django.db import models

# task-1 (creating artist ,album and queryset)


# task-2
class PollManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('stage_name')
# task-2


class Artist(models.Model):

    stage_name = models.CharField(max_length=100, unique=True, blank=False)

    social_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return "Stage_name =" + self.Stage_Name + "Social_link = " + self.Social_link

        # task-2
    objects = PollManager()

    def approved_albums(self):
        return self.album_set.filter(album_is_approved=True).count()

        # task-2


class Album(models.Model):

    artist_fk = models.ForeignKey(Artist, on_delete=models.CASCADE)

    album_name = models.CharField(
        max_length=200, default="New Album", verbose_name="New Album")

    creation_time = models.DateTimeField('time created', unique=True)

    release_time = models.DateTimeField('publish time')

    album_cost = models.DecimalField(max_digits=20, decimal_places=2)

    # Task-2
    album_is_approved = models.BooleanField(
        default=True, help_text="Approve the album if its name is not explicit")

    def __str__(self):
        return "name = " + self.album_name + " Artist = " + self.artist_fk.Stage_name

    def time_zone(self):
        return self.release_Time <= timezone.now()

    def time_zone(self):
        return self.release_Time <= timezone.now() - datetime.timedelta(days=1)
