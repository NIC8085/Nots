from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Note


#def home(request):
#    return render(request, 'web/home.html', {})

class NoteView(ListView):
    model = Note
    template_name = 'web/home.html'


class NoteDetailView(DetailView):
    model = Note
    template_name = 'web/details.html'


class NoteEditView(UpdateView):
    model = Note
    template_name = 'web/edit.html'
    fields = '__all__'


class NoteAddView(CreateView):
    model = Note
    template_name = 'web/add.html'
    fields = '__all__'

    def form_valid(self, form):
        # kod przetwarzania formularza
        note = form.save()
        return redirect('NotsApp:details', pk=note.pk)
