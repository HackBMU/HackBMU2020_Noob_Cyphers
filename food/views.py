from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"index.html")
def welcome(request):
    return render(request,"index2.html")