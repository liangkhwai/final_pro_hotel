from django.db import models
from django.contrib.auth.models import User
from creditcards.models import CardNumberField,CardExpiryField,SecurityCodeField

class Customer(models.Model):
    cust_id = models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    account = models.OneToOneField(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255,blank=True)
    age = models.DateField()
    gender = models.CharField(max_length=255)
    tel = models.CharField(max_length=10)
    address = models.TextField()

class RoomType(models.Model):
    type_id = models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    bed = models.CharField(max_length=255,blank=True,null=True)
    price = models.IntegerField(blank=True,default=0)
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='upload/images/',height_field=None,width_field=None,max_length=100,blank=True,null=True)
    description = models.TextField()
    limit_people = models.IntegerField(default=0)
    
    def __str__(self):
         return self.name
    
class Rooms(models.Model):
    room_id = models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    type = models.ForeignKey(RoomType,on_delete=models.SET_NULL,null=True)
    description = models.TextField()
    status = models.CharField(max_length=255)
    
class Transaction(models.Model):
    trans_id = models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    tran_date = models.DateTimeField(auto_now_add=True)
    cust = models.CharField(max_length = 255,null=True)
    roomtype = models.CharField(max_length = 255,null=True)
    room_id = models.CharField(max_length = 255,null=True)
    total = models.IntegerField(null=True)
    status = models.CharField(max_length = 255,null=True)

class Booking(models.Model):
    booking_id = models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    cust = models.ForeignKey(Customer,on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    date_in = models.DateField()
    date_out = models.DateField()
    total_payment = models.CharField(max_length=255)
    status = models.CharField(max_length=255,blank=True,default="ยังไม่ชำระเงิน")
    transection = models.OneToOneField(Transaction,on_delete=models.SET_NULL,null=True)


class Payment(models.Model):
    pay_id = models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    cust = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    pay_number =CardNumberField(('card number'),null=True,max_length=16)    
    pay_expiry =CardExpiryField(('expiration date'),null=True,max_length=4)    
    pay_code =CardNumberField(('security code'),null=True,max_length=3)    
    pay_amount = models.IntegerField(default=10000)
    
    

class MultiImage(models.Model):
    image = models.ImageField(null=True)
    type = models.ForeignKey(RoomType,on_delete=models.CASCADE,null = True)
    
    




    


    