from django.contrib import admin
from .models import Album
# Register your models here.


class approvedalbumcolumn(admin.StackedInline):
    model = Album
    extra = 1


class readonlyalbum(admin.ModelAdmin):
    readonly_fields = ('creation_time',)


admin.site.register(Album, readonlyalbum)
