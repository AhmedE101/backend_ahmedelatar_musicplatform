from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist
from .forms import ArtistForm
from django.views.generic import View
from django.contrib.auth.decorators import login_required


def list_artist(request):
    context = {'artist_list':  Artist.objects.all()}
    return render(request, 'artists/fetch.html', context)


def create_artist(request):

    passed = 1
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():

            form.save()
            return HttpResponse("thanks you, the record added successful.")
        else:
            passed = 0

    else:
        form = ArtistForm()

    return render(request, 'artists/add_artist.html', {'form': form, 'ok': passed})
