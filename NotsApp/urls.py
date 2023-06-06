from django.urls import path
from . import views
from .views import note_list

app_name = 'blog'
urlpatterns = [
    path('', note_list.as_view(), name='notes')

]