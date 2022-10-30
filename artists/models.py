from django.db import models


# task-1 (creating artist ,album and queryset)


class Artist(models.Model):

    stage_name = models.CharField(max_length=100, unique=True, blank=False)

    social_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return "Stage_name =" + self.stage_name + "Social_link = " + self.social_link

    def approved_albums(self):
        return self.album_set.filter(album_is_approved=True).count()
