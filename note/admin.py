from django.contrib import admin

from note.models import (
    NoteBook,
    Task
)

@admin.register(NoteBook)
class NoteBookAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class NoteBookAdmin(admin.ModelAdmin):
    pass
