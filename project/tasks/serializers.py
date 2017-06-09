from rest_framework import serializers

from .models import Task

from users.serializers import UserSerializer
from users.models import User


class TaskSerializer(serializers.ModelSerializer):
    creator = UserSerializer(source='author', read_only=True)
    nemo = serializers.SerializerMethodField(source='get_nemo', read_only=True)

    def get_nemo(self, obj):
        return obj.author.first_name + obj.author.last_name

    class Meta:
        model = Task
        fields = ['id', 'nemo', 'author', 'creator', 'task_title', 'task_description',
                  'start_date', 'expired_date', 'is_done']



        # extra_kwargs = {
        #     'id': {'read_only': True},
        #     'creator': {'read_only': True},
        #     'nemo': {'read_only': True},
        #     'task_title': {'required': True},
        #     'start_date': {'read_only': True}
        # }
