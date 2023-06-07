from django import forms
from .models import Note


#class AddNote(forms.Form):
#    class Meta:
#        model = Note
#        fields = ['title', 'author', 'priority', 'content']
#        widgets = {
#            'title': forms.TextInput(attrs={'class': 'input title'}),
#            'author': forms.TextInput(attrs={'class': 'input title'}),
#            'priority': forms.TextInput(attrs={'class': 'priority'}),
#            'content': forms.TextInput(attrs={'class': 'text'}),
#        }
