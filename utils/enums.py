from enum import Enum
from django.db.models import IntegerChoices

class NoteType(IntegerChoices):
    TODO = 1, "todo"
    SimpleNote = 2, "simple_note"


class TaskState(IntegerChoices):
    DONE = 1, "done"
    PAUSE = 2, "pause"
    DOING = 3, "doing"
    NOTSTARTED = 4, "not_started"


