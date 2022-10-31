from django.contrib import admin
from .models import Album
# Register your models here.


class readonlyalbum(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Album, readonlyalbum)
