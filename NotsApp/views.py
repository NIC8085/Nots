from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Note
class note_list(ListView):
    model = Note
    template_name = 'web/index.html'
