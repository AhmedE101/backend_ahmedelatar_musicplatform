from django.contrib import admin
from artists.models import Artist
from album.models import Album

# Register your models here.
admin.site.register(Artist)
admin.site.register(Album)
