from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('welcome',views.welcome,name="welcome"),
    path('welcome/aligarh',views.aligarh,name="aligarh"),
    path('welcome/delhi',views.delhi,name="delhi"),
    path('welcome/agra',views.agra,name="agra"),
    path('welcome/milkbar',views.milkbar,name="milkbar"),
    path('welcome/gravity',views.gravity,name="gravity"),
    path('welcome/sorrento',views.sorrento,name="sorrento"),
    path('welcome/karim',views.karim,name="karim")
]