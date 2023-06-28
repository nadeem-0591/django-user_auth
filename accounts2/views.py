from django.shortcuts import render, redirect
from .models import emplyee
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout


def home(request):
    username = request.session.get('username')
    return render(request, 'index.html', {'username': username})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']
        if emplyee.objects.filter(username=username).exists():
            return HttpResponse('User already exists')

        user = emplyee.objects.create(username=username, paswword=password, email=email, role=role)
        user.save()
        print('created successfully')

        return redirect('home')
    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = emplyee.objects.filter(username=username, paswword=password).first()
        if user:
            request.session['username'] = user.username
            return redirect('home')
        else:
            return HttpResponse('Invalid credentials')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('home')
