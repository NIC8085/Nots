from django.urls import path
#from . import views
#from .views import note_list
from .views import NoteView


app_name = 'blog'
urlpatterns = [
    #path('', views.home, name='home')
    path('', NoteView.as_view(), name='home')

]