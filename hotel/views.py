from hotel.models import Accounts, Customer, RoomType, Rooms
from .forms import *
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.




def home(req):
    return render(req,'home.html')

def register(req):
    if req.method == 'POST':
        cusForm = CustomerClassForm(req.POST)
        accForm = AccountClassForm(req.POST)
               
        print(cusForm,accForm)
        if cusForm.is_valid() and accForm.is_valid():
            print('asdsdsdsdsdsdsdsd')
            cusData = cusForm.cleaned_data
            cusAcc = accForm.cleaned_data    
            acc = Accounts()
            cus = Customer()
            acc.type = "user"
            acc.username = cusAcc['username']
            acc.password = cusAcc['password']
            cus.name = cusData['name']
            cus.age = cusData['age']
            cus.gender = cusData['gender']
            cus.tel = cusData['tel']
            cus.address = cusData['address']

            acc.save()
            cus.account = acc
            cus.save()
            
        print('nononono')
        return HttpResponseRedirect(reverse('home'))
    cusForm = CustomerClassForm()
    accForm = AccountClassForm()
    context = {'cusForm':cusForm,'accForm':accForm}
    return render(req,'member/register.html',context)


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


def addrooms(req):
    if req.method == 'POST':
        roomForm = AddRoomsClassForm(req.POST)
        if roomForm.is_valid():
            data = roomForm.cleaned_data
            room = Rooms()
            room.price = data['price']
            room.description = data['description']
            room.status = data['status']
            room.type = data['type']
            room.save()      

            print('success add rooms')
        return HttpResponseRedirect(reverse('home'))
    roomForm = AddRoomsClassForm()
    context = {'roomForm':roomForm}
    return render(req,'rooms/addrooms.html',context)

def addtype(req):
    if req.method == 'POST':
        typeForm = AddRoomsTypeForm(req.POST)
        if typeForm.is_valid():
            data = typeForm.cleaned_data
            type = RoomType()
            type.name = data['name']
            type.description = data['description']
            type.save()
            print('success add type')
        return HttpResponseRedirect(reverse('home'))
    typeForm = AddRoomsTypeForm()
    context = {'typeForm':typeForm}
    return render(req,'rooms/addtype.html',context)
    

