from django.contrib import admin
from .models import Artist


class displayadmin(admin.ModelAdmin):
    list_display = ('stage_name', 'social_link', 'approved_albums')


# Register your models here.
admin.site.register(Artist, displayadmin)
