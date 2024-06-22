from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin, 
    RetrieveModelMixin, 
    DestroyModelMixin
)
from rest_framework.viewsets import (
        ModelViewSet,
        GenericViewSet,     
)


from note.serializers import (
    NoteBookSerializer,
    TaskSerializer
)
from note.models import (
    NoteBook,
    Task
)
from utils.paginations import CustomPageNumberPagination

class NoteBookView(ModelViewSet):
    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializer
    pagination_class = CustomPageNumberPagination

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = CustomPageNumberPagination

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)