from django.shortcuts import render,redirect
from .models import City,Restaurants,RestaurantsDelhi,RestaurantsAgra
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth

# Create your views here.
def home(request):
    return render(request,"index.html")
def welcome(request):
    return render(request,"index2.html")
def error(request):
    return render(request,'error.html')

@login_required(login_url='/welcome/error')
def aligarh(request):
    city = City.objects.get(id=1)
    rests = Restaurants.objects.all()
    return render(request,'city.html',{'city':city,'rests':rests})

@login_required(login_url='/welcome/error')
def delhi(request):
    city2 = City.objects.get(id=2)
    rests2 = RestaurantsDelhi.objects.all()
    return render(request,'city.html',{'city':city2,'rests':rests2})

@login_required(login_url='/welcome/error')
def agra(request):
    city3 = City.objects.get(id=3)
    rests3 = RestaurantsAgra.objects.all()
    return render(request,'city.html',{'city':city3})