from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from . import forms
from .models import AddTask
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'login/')
def homepage(request):
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
        print(alltasks)
        return render(request, 'homepage.html', {'tasks':alltasks, 'form': form})
