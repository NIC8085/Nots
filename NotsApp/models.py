from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
# Create your models here.


class Priority(models.Model):
    title = models.CharField(max_length=20)
    shortcut = models.CharField(max_length=15, default='')
    color = models.CharField(max_length=15)
    weight = models.IntegerField(default=0, validators=[MaxValueValidator(6), MinValueValidator(0)])

    priorityManager = models.Manager()

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=50)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name='notes')

    noteManager = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details', args=(str(self.id)))

