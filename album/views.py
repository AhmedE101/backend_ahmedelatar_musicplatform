from django.shortcuts import render
from .forms import AlbumForm
from django.views.generic import FormView
from django.http import HttpResponse

# Create your views here.


class create_album(FormView):
    template_name = 'album/add_album.html'
    form_class = AlbumForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("thanks you, the record added successful.")
        else:
            return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
