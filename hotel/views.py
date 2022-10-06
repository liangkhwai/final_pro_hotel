from pydoc import resolve
from hotel.models import Customer, RoomType, Rooms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as auth_login
from .forms import *
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.template import RequestContext, Template
from django.shortcuts import redirect
from datetime import date, datetime
from django.core import serializers
from django.db.models import Q

# Create your views here.





def home(req):
    if req.method == 'POST':
        form = SearchForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data['people'])
            if data['date_in'] > data['date_out']:
                messages.add_message(req,messages.ERROR,'กรุณากรอกวันที่เข้าให้น้อยกว่าวันที่ออก')
                return redirect('home')
            if data['people'] == '4':
                rooms = RoomType.objects.all().filter(limit_people = 4)
            else:
                rooms = RoomType.objects.all().filter(~Q(limit_people = 4))
            response = render(req,'rooms/user_rooms.html',{'roomss':rooms})
            response.set_cookie('date_in',data['date_in']) 
            response.set_cookie('date_out',data['date_out']) 
            response.set_cookie('people',data['people'])
            return response   
    else:
        form = SearchForm()
    
    
    return render(req,'home.html',{'form':form})
    
    
    
    



def register(req):
    if req.method == 'POST':
        cusForm = CustomerClassForm(req.POST)
        accForm = RegisterForm(req.POST)
               
        print(cusForm,accForm)
        if cusForm.is_valid() and accForm.is_valid():
            print('asdsdsdsdsdsdsdsd')
            cusData = cusForm.cleaned_data
            cus = Customer()            
            account = accForm.save()
            cus.firstname = cusData['firstname']
            cus.lastname = cusData['lastname']
            cus.age = cusData['age']
            cus.gender = cusData['gender']
            cus.tel = cusData['tel']
            cus.address = cusData['address']
            cus.account = account
            cus.save()
            return HttpResponseRedirect(reverse('home'))        
    else:
        cusForm = CustomerClassForm()
        accForm = RegisterForm()
    context = {'cusForm':cusForm,'accForm':accForm}
    return render(req,'member/register.html',context)


def login_user(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = authenticate(username=username,password=password)
        
        if user is not None:
            check = auth_login(req,user)
            req.session['user'] = user.id
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('home'))
        
    return render(req,'member/login.html')

def logout_user(req):
    logout(req)
    return HttpResponseRedirect(reverse('home'))

def editcustomer(req,pk):
    customer = Customer.objects.get(cust_id=pk)
    if req.method == 'POST':
        form = UpdateCustomerForm(req.POST,instance=customer)
        if form.is_valid():
            form.save()    
            print('HIHI')
            return HttpResponseRedirect(reverse('home'))
    
    form = UpdateCustomerForm(instance=customer)
    context = {
        'form':form
    }
    print('FLASE')
    return render(req,'member/editcustomer.html',context)


def editpassword(req,pk):
    account = User.objects.get(id = pk)
    if req.method == 'POST':
        form = RegisterForm(req.POST,instance=account)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = RegisterForm(instance=account)
    context = {
        'form':form
    }
    return render(req,'member/editpassword.html',context)    



def addrooms(req):
    if req.method == 'POST':
        roomForm = AddRoomsClassForm(req.POST)
        print(roomForm)
        if roomForm.is_valid():
            data = roomForm.cleaned_data
            room = Rooms()
            # room.price = data['price']
            room.description = data['description']
            room.status = data['status']
            room.type = data['type']
            room.save()      

            print('success add rooms')
        return HttpResponseRedirect(reverse('home'))
    roomForm = AddRoomsClassForm()
    context = {'roomForm':roomForm}
    return render(req,'rooms/addrooms.html',context)

def editrooms(req,pk):
    rooms = Rooms.objects.all().filter(type_id = pk)     
    type = RoomType.objects.get(type_id = pk)
    if req.method == 'POST':
        form = Addroom(req.POST)
        print(form)
        
        if form.is_valid():
            data = form.cleaned_data
            room = Rooms() 
            room.description = data['description']
            room.status = data['status']
            room.type = type
            room.save()
            return redirect('editrooms',pk=pk)
    else:
        form = Addroom()
    context = {
        'form':form,
        'rooms':rooms
    }
    return render(req,'rooms/editrooms.html',context)

def editroom(req,pk,fk):
    room = Rooms.objects.get(room_id = fk)
    if req.method == 'POST':
        form = AddRoomsClassForm(req.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('editrooms',pk=pk)
    form = AddRoomsClassForm(instance=room)
    context = {
        'form':form,
        'room':room
    }
    return render(req,'rooms/editroom.html',context)

def deleteroom(req,pk,fk):
    room = Rooms.objects.get(room_id = pk)
    room.delete()
    # return HttpResponseRedirect(reverse('fetchrooms'))
    return redirect('editrooms',pk=fk)


def deletetype(req,pk):
    type = RoomType.objects.get(type_id = pk)
    type.delete()
    return HttpResponseRedirect(reverse('fetchrooms'))


def addtype(req):
    if req.method == 'POST':
        typeForm = AddRoomsTypeForm(req.POST)
        if typeForm.is_valid():
            data = typeForm.cleaned_data
            type = RoomType()
            type.name = data['name']
            type.description = data['description']
            type.price = data['price']
            type.save()
            print('success add type')
        return HttpResponseRedirect(reverse('fetchrooms'))
    typeForm = AddRoomsTypeForm()
    context = {'typeForm':typeForm}
    return render(req,'rooms/addtype.html',context)

def edittype(req,pk):
    type = RoomType.objects.get(type_id = pk)
    if req.method == 'POST':
        form = AddRoomsTypeForm(req.POST,instance=type,files=req.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fetchrooms'))
        
    else:
        form = AddRoomsTypeForm(instance=type)
    context = {
        'form':form,
        'type':type
    }
    return render(req,'rooms/edittype.html',context)


def fetchrooms(req):
    type = RoomType.objects.all()
    if req.method == 'POST':
        form = AddRoomsTypeForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fetchrooms'))

    form = AddRoomsTypeForm()
    context = {
        'type':type,
        'form':form
    }
    return render(req,'rooms/fetchrooms.html',context)





def roomdetail(req,pk):
    typeCheck = RoomType.objects.get(type_id = pk)
    roomCheck = Rooms.objects.all().filter(type_id = pk,status = "ว่าง").count()
    
    context = {
        'type':typeCheck,
        'count':roomCheck
    }
    return render(req,'rooms/roomdetail.html',context)



def booking(req,pk):
    room_free = Rooms.objects.all().filter(type_id=pk,status = 'ว่าง').first()

    user = Customer.objects.get(account_id = req.session['user'])
    detail = RoomType.objects.get(type_id = pk)

    date_in = datetime.strptime(req.COOKIES['date_in'],'%Y-%m-%d').date()
    date_out = datetime.strptime(req.COOKIES['date_out'],'%Y-%m-%d').date()
    rental_day = date_out - date_in
    print(type(date_in))
    price = detail.price * rental_day.days
    remain_day = rental_day.days


    if req.method == 'POST':
        form = BookingForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            book = Booking()
            
            book.date_in = data['date_in']
            book.date_out = data['date_out']
            book.total_payment = room_free.type.price * (data['date_out'].day - data['date_in'].day)
            book.cust = user
            book.room = room_free
            book.save()
            room_free.status = "ไม่ว่าง"
            room_free.save()
            
    else:
        form = BookingForm()    
    context = {
        'form':form,
        'room_free':room_free,
        'date_in':date_in,
        'date_out':date_out,
        'detail':detail,
        'days':remain_day,
        'price':price
    }
    return render(req,'booking/booking.html',context)

    

