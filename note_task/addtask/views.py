from django.shortcuts import render, redirect
from . import forms

def addtask(request):
    if request.method == 'POST':
        form = forms.AddTaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/addtask/')
    else:
        form = forms.AddTaskForm()
        return render(request, 'addtask/AddTask.html', {'form': form})
