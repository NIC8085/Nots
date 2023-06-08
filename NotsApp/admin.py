from django.contrib import admin
from .models import Note, Priority

# Register your models here.


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'author', 'created')
    search_fields = ('title', 'content')
    ordering = ('priority', 'created', 'title')


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('title', 'shortcut', 'color', 'weight')
    search_fields = ('title', 'color', 'weight')
    ordering = ('weight', 'title', 'color')
