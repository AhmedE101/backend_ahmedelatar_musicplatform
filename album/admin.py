from django.contrib import admin
from .models import Album
# Register your models here.


class approved_albumcolumn(admin.StackedInline):
    model = Album
    extra = 1


class readonly_album(admin.ModelAdmin):
    readonly_fields = ('creation_time',)


admin.site.register(Album, readonly_album)
