from django.shortcuts import render
from .forms import AlbumForm
from django.views.generic import FormView
from django.http import HttpResponse

# Create your views here.


def create_album(request):

    passed = 1
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("thanks you, the record added successful.")
        else:
            passed = 0

    else:
        form = AlbumForm()

    return render(request, 'artists/add_album.html', {'form': form, 'ok': passed})
