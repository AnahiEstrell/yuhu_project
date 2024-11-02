from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from task.models import Task
from task.serializers import TaskSerializer
# from task.task import send_task_notification
from rest_framework.pagination import PageNumberPagination
from concurrent.futures import ThreadPoolExecutor


def index(request):
    return render(request, 'task/index.html')


def async_send_mail(subject, message, from_email, recipient_list):
    with ThreadPoolExecutor() as executor:
        executor.submit(
            send_mail,
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False
        )


class TaskPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page'
    max_page_size = 100


class TaskViewSet(viewsets.ViewSet):
    """
    ViewSet for tasks endpoints
    """
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        """GET endpoint tasks"""
        tasks = Task.objects.all()
        paginator = self.pagination_class()
        paginated_tasks = paginator.paginate_queryset(
            tasks,
            request,
            view=self
        )

        serializer = self.serializer_class(paginated_tasks, many=True)
        return paginator.get_paginated_response(serializer.data)

    def create(self, request):
        """POST endpoint tasks"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            async_send_mail(
                "Nueva tarea creada",
                f"La tarea '{task.titulo}' ha sido creada exitosamente.",
                settings.DEFAULT_FROM_EMAIL,
                [task.email]
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
            async_send_mail(
                "Tarea actualizada",
                f"La tarea '{task.titulo}' ha sido actualizada exitosamente.",
                settings.DEFAULT_FROM_EMAIL,
                [task.email]
            )
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """DELETE endpoint tasks"""
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
