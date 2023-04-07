from django.db import models

# Create your models here.

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=50, null=False)
    hotel_price = models.IntegerField(null=False,default= 0)

