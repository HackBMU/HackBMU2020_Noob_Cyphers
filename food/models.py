from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    headimg = models.ImageField(upload_to='pics')
    desc = models.TextField()
    img1 = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics')
    img3 = models.ImageField(upload_to='pics')
    img4 = models.ImageField(upload_to='pics')

class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')

class RestaurantsDelhi(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')

class RestaurantsAgra(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')

class MilkbarRev(models.Model):
    rev = models.TextField()
    revowner1 = models.CharField(max_length=100)
    revowner2 = models.CharField(max_length=100)

class GravityRev(models.Model):
    rev = models.TextField()
    revowner1 = models.CharField(max_length=100)
    revowner2 = models.CharField(max_length=100)

class SorrentoRev(models.Model):
    rev = models.TextField()
    revowner1 = models.CharField(max_length=100)
    revowner2 = models.CharField(max_length=100)

class KarimRev(models.Model):
    rev = models.TextField()
    revowner1 = models.CharField(max_length=100)
    revowner2 = models.CharField(max_length=100)
