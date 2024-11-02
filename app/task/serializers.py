from rest_framework import serializers
from task.models import Task
from datetime import date


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the task object"""

    def validate_fecha_vencimiento(self, value):
        if value < date.today():
            raise serializers.ValidationError(
                "La fecha de vencimiento debe ser posterior a la fecha actual."
            )
        return value

    class Meta:
        model = Task
        fields = [
            'id',
            'titulo',
            'email',
            'descripcion',
            'fecha_vencimiento',
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
