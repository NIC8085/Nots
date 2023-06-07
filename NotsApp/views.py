from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Note


#def home(request):
#    return render(request, 'web/home.html', {})

from django.views.generic import ListView
from .models import Note

class NoteView(ListView):
    model = Note
    template_name = 'web/home.html'
    context_object_name = 'notes'

    def get_queryset(self):
        queryset = super().get_queryset()
        priority_order = self.request.GET.get('priority', 'descending')

        if priority_order == 'ascending':
            queryset = queryset.order_by('priority__weight')
        else:
            queryset = queryset.order_by('-priority__weight')

        return queryset


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
