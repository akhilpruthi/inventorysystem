from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import userdata

# Create your views here.

def home(request):
    return render(request,'homepage.html')

def adduser(request):
    return render(request,'adduser.html')

def create(request):
    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        phone_number = request.POST['phonenumber']
        waranty = request.POST['waranty']
        obj = userdata.objects.create(name=name,address=address,phone_number=phone_number,waranty=waranty)
        obj.save()
        print("OBJECT::::::::::::::::::::::",obj)
        