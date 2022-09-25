from hotel.models import Accounts, Customer
from .forms import AccountClassForm, AccountForm, CustomerClassForm, CustomerForm
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
    return render(req,'register.html',context)


