from django.urls import path
from user import views


app_name = 'user'

urlpatterns = [
    path('api/user/me/', views.UserMeView.as_view(), name='me'),
    path('', views.index, name='index'),
]
