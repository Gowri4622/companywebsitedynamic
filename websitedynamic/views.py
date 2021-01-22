from django.shortcuts import render

from .models import Product

from .models import People

# Create your views here.

def home(request):
    context = {}
    return render(request, 'websitedynamic/home.html', context)

def products(request):
    context = {}

    context["products"] = Product.objects.all();

    return render(request, 'websitedynamic/products.html', context)    

def people(request):
    context = {}

    context["peoples"] = People.objects.all();

    return render(request, 'websitedynamic/people.html', context)  

def contactus(request):
    context = {}
    return render(request, 'websitedynamic/contactus.html', context)  

        


