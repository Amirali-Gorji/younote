from rest_framework import serializers

from note.models import (
    NoteBook,
    Task
)
from utils.enums import NoteType

class NoteBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteBook
        fields = '__all__'

    def to_representation(self, instance):
        instance = super().to_representation(instance)

        if instance['type'] == NoteType.TODO:
            tasks = Task.objects.filter(notebook=instance['id'])

            tasks_arr = []
            for task_obj in tasks:
                task = {    
                    'name': task_obj.name,
                    'state': task_obj.state
                }
                tasks_arr.append(task)
            instance['tasks'] = tasks_arr

        return instance

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_notebook(self, data):
        notebook_obj = data
        if notebook_obj.type != NoteType.TODO:
            raise serializers.ValidationError(f"notebook `{notebook_obj.id}` must be of type TODO to asign task to it")
        
        return data