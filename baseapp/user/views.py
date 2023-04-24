from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import userdata
from .forms import *
# from django.conf import settings
# from qrcode import *
# import time

# Create your views here.

def home(request):
    return render(request,'homepage.html')

def addUserPage(request):
    return render(request,'adduser.html')

def createUser(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        product_saledate = request.POST.get('product_saledate')
        obj = userdata.objects.create(name=name,address=address,phone_number=phone_number,product_saledate=product_saledate)
        obj.save()
        print("OBJECT::::::::::::::::::::::",obj.id)
        return redirect('../readUser/')

        
def readUser(request):
    context = userdata.objects.all()
    return render(request,"readUser.html",{'context':context})

def editUser(request,id):
    context = userdata.objects.get(id = id)
    print("name :::::::::::::::::::::::::::",context.id)
    # print("NAME::::::::::::::::",object.name)
    return render(request,'editUser.html',{'context':context})

def updateUser(request,id):
    object=userdata.objects.get(id=id)
    form=userDataform(request.POST,instance=object)
    print("FORM SUBMITTED::::::::::::",form)
    if form.is_valid():
        print("FORM IS VALID +++++++++++++++++",)
        form.save()
        object=userdata.objects.all()
        print("OBJECT IS VALID^^^^^^^^^^^^^^^^^:::",object)
        return redirect('../../readUser/')
    
def deleteUser(request,id):
    object = userdata.objects.filter(id=id)
    object.delete()
    return redirect('readUser')

# def qrGenerator(request,id):
#     context = userdata.objects.get(id = id)
#     data = request.POST[context]
#     img = make(data)
#     img_name = 'qr' + str(time.time()) + '.png'
#     img.save(settings.MEDIA_ROOT + '/' + img_name)
#     print("IMAGE SAVED:::::::::::::::::::")
#     return render(request, 'qrcode.html', {'img_name': img_name})
    