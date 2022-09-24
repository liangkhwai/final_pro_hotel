from .forms import RegisterClassForm
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.




def home(req):
    return render(req,'home.html')

def Register(req):
    if req.method == 'POST':
        form = RegisterClassForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = RegisterClassForm()
            user.name = req.POST.get('name')
            user.username = req.POST.get('username')
            user.password = req.POST.get('password')
            user.type = 'user'
            user.age = req.POST.get('age')
            user.gender = req.POST.get('gender')
            user.tel = req.POST.get('tel')
            user.address = req.POST.get('address')
            return HttpResponseRedirect(reverse('base.html'))


