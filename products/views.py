from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
    return HttpResponse(Product.name)

def price(request):
    print(format('Hello Price M'))
    return  HttpResponse('Price Module')

