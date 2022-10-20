from django.contrib import admin
from .models import Artist, Album

# Register your models here.
# task-2


class DisplayInline(admin.StackedInline):
    model = Album
    extra = 1


class ReadOnlyAlbum (admin.ModelAdmin):
    readonly_fields = ('creation_time',)


class DisplayArtist(admin.ModelAdmin):
    list_display = ('stage_name', 'social_link', 'approved_albums')
    inlines = [DisplayInline]


admin.site.register(Artist, DisplayArtist)
admin.site.register(Album, ReadOnlyAlbum)
