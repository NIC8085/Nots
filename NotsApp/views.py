from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Note


#def home(request):
#    return render(request, 'web/home.html', {})

class NoteView(ListView):
    model = Note
    template_name = 'web/home.html'


class NoteDetailView(DetailView):
    model = Note
    template_name = 'web/details.html'


class NoteEditView(DetailView):
    model = Note
    template_name = 'web/edit.html'
