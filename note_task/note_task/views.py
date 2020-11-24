from django.http import HttpResponse
from django.shortcuts import render
from addtask.models import AddTask

def homepage(request):
    alltasks = AddTask.objects
    return render(request, 'homepage.html', {'tasks':alltasks})
