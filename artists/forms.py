from django import forms
from dataclasses import field
from django.forms import ModelForm
from .models import Artist
from datetime import datetime


class ArtistForm (ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

    def is_valid(self) -> bool:
        name = self.data['stage_name']
        records = Artist.objects.filter(stage_name=name).count()
        if records > 0:
            return False

        return super().is_valid()
