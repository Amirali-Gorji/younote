from django.db import models
from utils.enums import NoteType, TaskState


class NoteBook(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    type = models.IntegerField(choices=NoteType.choices)
    state = models.IntegerField(default=TaskState.NOTSTARTED, choices=TaskState.choices)
    attachment = models.FileField(null=True, upload_to='upload/')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class Task(models.Model):
    notebook = models.ForeignKey(NoteBook, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    state = models.IntegerField(default=TaskState.NOTSTARTED, choices=TaskState.choices)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
