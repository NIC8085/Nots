from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Note
from django.core.paginator import Paginator, EmptyPage


class NoteView(ListView):
    model = Note
    template_name = 'web/home.html'
    paginate_by = 10  # Określa ilość notatek na stronie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notes = context['object_list']
        paginator = Paginator(notes, self.paginate_by)
        page_number = self.request.GET.get('page')

        try:
            page_obj = paginator.get_page(page_number)
        except EmptyPage:
            page_obj = paginator.get_page(1)  # Wyświetl pierwszą stronę, jeśli numer strony jest nieprawidłowy

        context['page_obj'] = page_obj
        return context


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
