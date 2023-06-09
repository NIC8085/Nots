from django.urls import path
from .views import NoteView, NoteDetailView, NoteEditView, NoteAddView


app_name = 'NotsApp'

urlpatterns = [
    path('', NoteView.as_view(), name='home'),
    path('details/<int:pk>', NoteDetailView.as_view(), name='details'),
    path('edit/<int:pk>', NoteEditView.as_view(), name='edit'),
    path('add/', NoteAddView.as_view(), name='add'),
]