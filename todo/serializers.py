from rest_framework import serializers
from .models import ToDoModel

class ToDoModelSerializers(serializers.ModelSerializer):
    # task_name = serializers.CharField()
    # task_description = serializers.CharField()
    # task_start_time = serializers.TimeField()
    # task_end_time = serializers.TimeField()
    # done = serializers.BooleanField()
    class Meta:
        model =ToDoModel
        fields = ('task_name','task_description','task_start_time','task_end_time','done')