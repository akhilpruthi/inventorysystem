from django.contrib import admin
from django.urls import path,include
from user import views

urlpatterns = [
    path('',views.home,name ="home"),
    path('adduser',views.adduser,name ="adduser"),
    path('create',views.create,name ="create"),
]
