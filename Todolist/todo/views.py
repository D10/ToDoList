from django.shortcuts import render
from django.views.generic import ListView

from .models import ToDo, Priority, Status


class ToDoList(ListView):
    model = ToDo
    template_name = 'index.html'
    context_object_name = 'todo'
