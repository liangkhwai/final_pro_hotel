from django.db import models

# Create your models here.

class Accounts(models.Model):
    account_id = models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    type = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Customer(models.Model):
    cust_id = models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    account = models.OneToOneField(Accounts,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.DateField()
    gender = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    address = models.TextField()
    

    

class RoomType(models.Model):
    type_id = models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    price = models.IntegerField(blank=True,default=0)
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Rooms(models.Model):
    room_id = models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    type = models.ForeignKey(RoomType,on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=255)
    

class Booking(models.Model):
    booking_id = models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    cust = models.ForeignKey(Customer,on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    date_in = models.DateTimeField()
    date_out = models.DateTimeField()
    total_payment = models.CharField(max_length=255)
    status = models.CharField(max_length=255,blank=True)


class Payment(models.Model):
    pay_id = models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    cust = models.ForeignKey(Customer,on_delete=models.CASCADE)
    method = models.CharField(max_length=255) #ประเภทการชำระเงิน เงินสด เงินโอน
    amount = models.FloatField()
    date = models.DateTimeField()
    
class Transaction(models.Model):
    trans_id = models.BigAutoField(primary_key=True,auto_created=True,serialize=False)
    tran_date = models.DateTimeField(auto_now_add=True)
    cust = models.ForeignKey(Customer,on_delete=models.CASCADE)
    pay = models.OneToOneField(Payment,on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE)






    


    