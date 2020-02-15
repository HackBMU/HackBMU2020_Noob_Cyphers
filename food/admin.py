from django.contrib import admin
from .models import City,Restaurants,RestaurantsDelhi,RestaurantsAgra

# Register your models here.

admin.site.register(City)
admin.site.register(Restaurants)
admin.site.register(RestaurantsDelhi)
admin.site.register(RestaurantsAgra)

