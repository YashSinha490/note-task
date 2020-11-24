from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from . import forms
from .models import AddTask

def homepage(request):
    if request.method == 'POST':
        form = forms.AddTaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/homepage/')
    else:
        alltasks = AddTask.objects
        form = forms.AddTaskForm()
        return render(request, 'homepage.html', {'tasks':alltasks, 'form': form})
