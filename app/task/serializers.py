from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the task object"""

    class Meta:
        model = Task
        fields = [
            'id',
            'titulo',
            'email',
            'descripcion',
        ]
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        """Update only titulo and descripcion fields"""
        instance.titulo = validated_data.get(
            'titulo',
            instance.titulo
        )
        instance.descripcion = validated_data.get(
            'descripcion',
            instance.descripcion
        )
        instance.save()
        return instance
