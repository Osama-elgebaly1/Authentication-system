from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django import forms
# Create your views here.


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{})
        else:
            user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password,
                                        )
            user.first_name = firstname
            user.last_name = lastname
            user.save()
        
            return redirect('/')
    else:
        return render(request,'register.html',{})


def Login(request):
    pass

def logout(request):
    pass

def profile(request):
    pass