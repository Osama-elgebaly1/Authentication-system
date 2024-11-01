from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django import forms
from django.http import HttpResponse
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


def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,
                            password=password)
        if user is not None:

            login(request,user)
            html_content = '''
        <html>
            <body>
                <h1>Welcome!</h1>
                <h3> <a href="{% url 'logout' %}">Logout</a></h3>
            </body>
        </html>
        '''
            return HttpResponse(html_content)
        
        else:
            return HttpResponse('User does not exist ')
    else:
        return render(request,'login.html',{})


def out(request):
    pass

def profile(request):
    pass