from django.urls import path
#from . import views
#from .views import note_list
from .views import NoteView, NoteDetailView, NoteEditView


app_name = 'NotsApp'

urlpatterns = [
    #path('', views.home, name='home')
    path('', NoteView.as_view(), name='home'),
    path('details/<int:pk>', NoteDetailView.as_view(), name='details'),
    path('edit/<int:pk>', NoteEditView.as_view(), name='edit')
]