from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def addtask(request):
    return render(request, 'AddTask.html')
