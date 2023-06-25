from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages


from django.contrib.auth import login,authenticate,logout



# Create your views here.
def home(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():

            messages.error(request, 'Username already exists.')

        else:
            user = User.objects.create_user(username=username, password=password)
            # Set user role based on your requirements
            # user.role = role
            # user.save()
            messages.success(request, 'User created successfully.')

        return redirect('home')
    return render(request,'register.html')
def login_user(request):
        
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user=authenticate(username=username, password=password)
            if user is not None:
                 login(request,user)
                 return redirect('home')
            else:
                 return render(request,'login.html','user succes full')
            



        return render(request,'login.html')
def logout_user(request):
     logout(request)
     return redirect('home')