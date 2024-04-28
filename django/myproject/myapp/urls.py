from django.urls import path
from .views import *

urlpatterns = [
    path('add_user/', addUser, name='addUser'),
    path('add_task/', addTask, name='addTask'),
    path('users/', listUser, name='listUser'),
    path('tasks/', listTask, name='listTask'),
    path('task_description/<int:task_id>/', task_description, name='task_description'),
    path('user_description/<int:user_id>/', user_description, name='user_description'),
]
