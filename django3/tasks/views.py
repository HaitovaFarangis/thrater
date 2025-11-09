from django.shortcuts import render, HttpResponse
from .models import Task

def index(request):
    return render(request, 'index.html')

def end(request):
    return HttpResponse('<h1>The End</h1>')

def home(request):
    # select * from tasks -->SQL
    # ORM ---> Object Relational  Mapping
    task_list = Task.objects.all()
    return render(request, 'main.html', {"tasks":task_list, "age":22})

    

# Create your views here.
