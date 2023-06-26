from django.shortcuts import render,redirect
from .models import customer
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout


def home(request):
    username = request.session.get('username')
    return render(request, 'index.html', {'username': username})
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']
        if customer.objects.filter(username=username).exists():
            return HttpResponse('User already exists')
        


        user = customer.objects.create(username=username, password=password, role = role,email =email)
        user.save()
        # login(request, user)
        # return HttpResponse('Created successfully')
        print('created suscess')

          
        return redirect('home')
    return render(request,'register.html')
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = customer.objects.filter(username=username, password=password).first()
        if user:
            request.session['username'] = user.username
            return redirect('home')
        else:
            return HttpResponse('Invalid credentials')
    return render(request, 'login.html')

def logout_user(request):
     logout(request)
     return redirect('home')