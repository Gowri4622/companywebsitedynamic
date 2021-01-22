from django.db import models
from django.contrib import admin

# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=100)
    productprice = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/') 

class ProductAdmin(admin.ModelAdmin):
    list_display = ('productname', 'productprice')

class People(models.Model):
    name = models.CharField(max_length=100)
    position= models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/') 

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
