from itertools import chain
from django.db import models

# Create your models here.


class Guest(models.Model):
    guest_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    guest_name = models.CharField(max_length=60)
    guest_email = models.EmailField(unique=True,max_length=255)
    guest_address = models.TextField(max_length=255,null=True)
    guest_tel = models.CharField(max_length=10)
    guest_pwd = models.CharField(max_length=255)
    
    
class Room(models.Model):
    room_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    room_type = models.CharField(max_length=50)
    room_price = models.IntegerField()
    room_description = models.TextField(max_length=255,null=True)
    room_img = models.ImageField()



    