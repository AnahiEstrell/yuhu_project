from django.urls import path
from task.views import TaskViewSet, index

task_list = TaskViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

task_detail = TaskViewSet.as_view({
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('dashboard/', index, name='dashboard'),
    path('api/tasks/', task_list, name='task-list'),
    path('api/tasks/<str:pk>', task_detail, name='task-detail'),
]
