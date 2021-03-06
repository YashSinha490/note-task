from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import AddTask
from django.contrib.auth.decorators import login_required
from django import template
from django.db.models import Q

register = template.Library()

@login_required(login_url = 'login/')
def homepage(request):
    count = AddTask.objects.filter(user=request.user).count()
    if request.method == 'POST':
        form = forms.AddTaskForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.user = request.user
            instance.save()
            return redirect('/homepage/')
        else:
            alltasks = AddTask.objects.filter(user=request.user)
            form = forms.AddTaskForm()
            return render(request, 'homepage.html', {'error':'make sure the input in correct', 'tasks':alltasks, 'form': form, 'count':count})
    else:
        alltasks = AddTask.objects.filter(user=request.user)
        form = forms.AddTaskForm()
        return render(request, 'homepage.html', {'tasks':alltasks, 'form': form, 'count':count})

@login_required
def removeTask(request, task_id):
    task = get_object_or_404(AddTask, pk=task_id)
    if request.user == task.user:
        AddTask.objects.filter(id = task_id).delete()
        return redirect('/homepage/')

@login_required
def search(request):
    count = AddTask.objects.filter(user=request.user).count()
    if request.method == 'POST':
        form = forms.AddTaskForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.user = request.user
            instance.save()
            return redirect('/homepage/')
        else:
            alltasks = AddTask.objects.filter(user=request.user)
            form = forms.AddTaskForm()
            return render(request, 'homepage.html', {'error':'make sure the input in correct', 'tasks':alltasks, 'form': form, 'count':count})
    if request.method == "GET":
        form = forms.AddTaskForm()
        search = request.GET.get('search')
        alltasks = AddTask.objects.all().filter(user = request.user, taskName = search)
        return render(request, 'homepage.html', {'tasks' : alltasks, 'form':form, 'count':count})

def about(request):
    return render(request, 'about.html')
