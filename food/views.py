from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import City,Restaurants,RestaurantsDelhi,RestaurantsAgra,MilkbarRev,GravityRev,SorrentoRev,KarimRev
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

@login_required(login_url='/welcome/error')
def milkbar(request):
    if request.method=='POST':
        a = request.POST.get('revtext')
        b = request.user.get_full_name()

        milkbarrev = MilkbarRev(rev=a,revowner1=b)
        milkbarrev.save()

        return redirect('milkbar')
    
    else:
        #Retrieve reviews from database
        reviews = MilkbarRev.objects.all()
        #For selecting img of rest obj 1 which is milkbar image
        rest = Restaurants.objects.get(id=1)
        #For changing link in reviews.html and selecting city 1 which is aligarh. Because this rest is in aligarh
        city = City.objects.get(id=1)
        city.name = city.name.lower()
        return render(request,'review.html',{'rest':rest,'city':city,'reviews':reviews})

@login_required(login_url='/welcome/error')
def gravity(request):
    if request.method=='POST':
        a = request.POST.get('revtext')
        b = request.user.get_full_name()

        gravityrev = GravityRev(rev=a,revowner1=b)
        gravityrev.save()

        return redirect('gravity')

    else:
        #Retrieve reviews from database
        reviews = GravityRev.objects.all()
        #For selecting img of rest obj 2 which is gravity image
        rest2 = Restaurants.objects.get(id=2)
        #For changing link in reviews.html and selecting city 1 which is aligarh. Because this rest is in aligarh
        city = City.objects.get(id=1)
        city.name = city.name.lower()
        return render(request,'review.html',{'rest':rest2,'city':city,'reviews':reviews})

@login_required(login_url='/welcome/error')
def sorrento(request):
    if request.method=='POST':
        a = request.POST.get('revtext')
        b = request.user.get_full_name()

        sorrentorev = SorrentoRev(rev=a,revowner1=b)
        sorrentorev.save()

        return redirect('sorrento')
    else:
        #Retrieve reviews from database
        reviews = SorrentoRev.objects.all()
        #For selecting img of rest obj 1 which is sorrentp image
        rest21 = RestaurantsDelhi.objects.get(id=1)
        #For changing link in reviews.html and selecting city 2 which is delhi. Because this rest is in delhi
        city = City.objects.get(id=2)
        city.name = city.name.lower()
        return render(request,'review.html',{'rest':rest21,'city':city,'reviews':reviews})

@login_required(login_url='/welcome/error')
def karim(request):
    if request.method=='POST':
        a = request.POST.get('revtext')
        b = request.user.get_full_name()

        karimrev = KarimRev(rev=a,revowner1=b)
        karimrev.save()

        return redirect('karim')
    else:
        #Retrieve reviews from database
        reviews = KarimRev.objects.all()
        #For selecting img of rest obj 2 which is karim image
        rest22 = RestaurantsDelhi.objects.get(id=2)
        #For changing link in reviews.html and selecting city 2 which is delhi. Because this rest is in delhi
        city = City.objects.get(id=2)
        city.name = city.name.lower()
        return render(request,'review.html',{'rest':rest22,'city':city,'reviews':reviews})
