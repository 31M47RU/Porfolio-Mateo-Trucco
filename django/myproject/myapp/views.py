from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def addUser(request):
    return render(request, 'adduser.html')

def addTask(request):
    return render(request, 'addtask.html')

def listTask(request):
    tasks = Task.objects.all()
    return render(request, 'listtask.html', {'tasks':tasks})

def listUser(request):
    users = User.objects.all()
    return render(request, 'listuser.html', {'users':users})

def task_description(request, task_id):
    tasks = get_object_or_404(Task, id=task_id)
    return render(request, 'taskdescription.html', {'task_id': task_id, 'tasks': tasks})

def user_description(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'userdescription.html', {'user_id': user_id, 'user': user})

#* HACER UN SOLO ARCHIVO QUE TENGA LOS DATOS DE USER Y TASK EN HTML
#* CONVINAR task_description Y user_description
#* TAMBIEN SE PUEDE JUNTAR ALGO MAS