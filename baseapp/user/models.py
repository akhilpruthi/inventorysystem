from django.db import models

# Create your models here.
class userdata(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    waranty = models.CharField(max_length=100)
