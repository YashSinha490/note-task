from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username = request.POST['username'])
            return render(request, 'authentication/signup.html', {'error' : 'Username already taken'})
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['email'], password = request.POST['password'])  # autheniicating with email now for notification, later change it to username and save email in database using models
            auth.login(request, user)
            return redirect('/homepage/')
    else:
        return render(request, 'authentication/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect("/homepage/")
        else:
            return render(request, 'authentication/login.html', {'error' : 'Username or password does not match!'})
    else:
        return render(request, 'authentication/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect("/homepage/")
