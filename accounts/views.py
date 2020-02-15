from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.db import IntegrityError
from django.http import HttpResponse


# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('welcome')
        else:
            messages.info(request,'Invalid Credentials !')
            return redirect('login')
    else:
        return render(request,'logindex.html')

def register(request):
    if  request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            print('user created')
            return redirect('login')
        except (IntegrityError,ValueError) :
            messages.info(request,'Username already taken !')
            return redirect('register')
    else:   
        return render(request,'regindex.html')

def logout(request):
    auth.logout(request)
    return redirect('/')