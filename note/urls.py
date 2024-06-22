from django.urls import path
from rest_framework import routers

from note.views import (
    NoteBookView,
    TaskView
)


router = routers.SimpleRouter()
router.register(r'notebook', NoteBookView, basename='notebook')
router.register(r'task', TaskView, basename='task')

urlpatterns = [

] + router.urls


