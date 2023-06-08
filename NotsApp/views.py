from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Note


class NoteView(ListView):
    model = Note
    template_name = 'web/home.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        priority = self.request.GET.get('priority', 'descending')

        if priority == 'ascending':
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

    def form_valid(self, form):
        note = form.save()
        return redirect('NotsApp:details', pk=note.pk)


class NoteAddView(CreateView):
    model = Note
    template_name = 'web/add.html'
    fields = '__all__'

    def form_valid(self, form):
        note = form.save()
        return redirect('NotsApp:details', pk=note.pk)
