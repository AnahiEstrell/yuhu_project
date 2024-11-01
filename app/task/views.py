from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response

from task.models import Task
from task.serializers import TaskSerializer
from task.task import send_task_notification


def index(request):
    """Renderiza la página principal HTML"""
    return render(request, 'task/index.html')


class TaskViewSet(viewsets.ViewSet):
    """
    ViewSet for tasks endpoints
    """
    serializer_class = TaskSerializer

    def list(self, request):
        """GET endpoint tasks"""
        tasks = Task.objects.all()
        serializer = self.serializer_class(tasks, many=True)
        return Response(serializer.data)

    def create(self, request):
        """POST endpoint tasks"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            send_mail(
                "Nueva tarea creada",
                f"La tarea '{task.titulo}' ha sido creada exitosamente.",
                settings.DEFAULT_FROM_EMAIL,
                [task.email],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """PUT endpoint tasks"""
        task = get_object_or_404(Task, pk=pk)
        serializer = self.serializer_class(
            task,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            task = serializer.save()
            send_mail(
                "Nueva tarea creada",
                f"La tarea '{task.titulo}' ha sido creada exitosamente.",
                settings.DEFAULT_FROM_EMAIL,
                [task.email],
                fail_silently=False,
            )
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """DELETE endpoint tasks"""
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
