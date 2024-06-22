from django.db import models
from utils.enums import NoteType, TaskState


class NoteBook(models):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    type = models.IntegerChoices(choices=NoteType.choices)
    state = models.IntegerChoices(choices=TaskState.choices)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class Task(models):
    note_book = models.ForeignKey(NoteBook, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    state = models.IntegerChoices(choices=TaskState.choices)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
