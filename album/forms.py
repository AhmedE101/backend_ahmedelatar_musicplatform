from django import forms
from django.forms import ModelForm
from .models import Album
from .widget import MyDateTimeInput


class AlbumForm(ModelForm):

    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'release_time': MyDateTimeInput()
        }
