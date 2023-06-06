from django.db import models

# Create your models here.


class Priority(models.Model):
    title = models.CharField(max_length=20)
    color = models.CharField(max_length=15)

    priorityManager = models.Manager()


class Note(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=50)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name='notes')

    noteManager = models.Manager()

    def __str__(self):
        return self.title
