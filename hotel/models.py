
from django.db import models

# Create your models here.


class Guest(models.Model):
    guest_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='guest Id')
    guest_name = models.CharField(max_length=60)
    guest_email = models.EmailField(unique=True,max_length=255)
    guest_address = models.TextField(max_length=255,null=True)
    guest_tel = models.CharField(max_length=10)
    guest_pwd = models.CharField(max_length=255)
    
    
class Room(models.Model):
    room_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='room Id')
    room_type = models.CharField(max_length=50)
    room_price = models.IntegerField()
    room_description = models.TextField(max_length=255,null=True)
    room_img = models.ImageField()


class Booking(models.Model):
    booking_id = models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='booking Id')
    guest_id = models.ForeignKey(Guest,on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking_checkin = models.DateTimeField()
    booking_checkout = models.DateTimeField()
    booking_status = models.CharField(max_length=255)
    booking_numOfpeople = models.IntegerField()


    