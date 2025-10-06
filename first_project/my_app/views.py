from django.shortcuts import render, HttpResponse
from .models import Todomodel

def home(request):
    return render(request, 'home.html')

def todos(request):
    items = Todomodel.objects.all()
    return render(request, 'todos.html', {'todos': items})
