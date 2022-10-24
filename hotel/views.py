from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as auth_login
from .forms import *
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.template import RequestContext, Template
from django.shortcuts import redirect
from datetime import date, datetime
from django.db.models import Q,Sum
from django.contrib.auth.decorators import login_required

# Create your views here.



def home(req):
    
       
    
    if req.method == 'POST':
        form = SearchForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data['people'])
            if data['date_in'] >= data['date_out']:
                # messages.add_message(req,messages.ERROR,'กรุณากรอกวันที่เข้าให้น้อยกว่าวันที่ออก')
                messages.error(req,"กรุณากรอกวันที่เข้าให้น้อยกว่าวันที่ออก")
                return redirect('home')

            if data['people'] == '4':
                rooms = RoomType.objects.all().filter(limit_people = 4)
            else:
                rooms = RoomType.objects.all()
                # .filter(~Q(limit_people = 4))
            response = render(req,'rooms/user_rooms.html',{'roomss':rooms})
            response.set_cookie('date_in',data['date_in']) 
            response.set_cookie('date_out',data['date_out']) 
            response.set_cookie('people',data['people'])
            return response   
    else:
        try:
            date_in = str(req.COOKIES['date_in'])
            date_out = str(req.COOKIES['date_out'])
            form = SearchForm(check_in = date_in,check_out= date_out)
        except:
            form = SearchForm()
            
    
    
    return render(req,'home.html',{'form':form})
    
    
    




def register(req):
    if req.method == 'POST':
        cusForm = CustomerClassForm(req.POST)
        accForm = RegisterForm(req.POST)
               
        print(cusForm,accForm)
        if cusForm.is_valid() and accForm.is_valid():
            print('asdsdsdsdsdsdsdsd')
            accData = accForm.cleaned_data
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
            
            user = authenticate(username=accData['username'],password=accData['password1'])
            auth_login(req,user)
            req.session['user'] = user.id
            
            return HttpResponseRedirect(reverse('home'))        
    else:
        cusForm = CustomerClassForm()
        accForm = RegisterForm()
    context = {'cusForm':cusForm,'accForm':accForm}
    return render(req,'member/register.html',context)

def contact(req):
    
    return render(req,'contact.html')



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
            return render(req,'member/login.html',{'error':"error"})
        
    return render(req,'member/login.html')

@login_required
def logout_user(req):
    logout(req)
    response = redirect('home')
    response.delete_cookie('people')
    response.delete_cookie('date_in')
    response.delete_cookie('date_out')
    return response

@login_required
def editcustomer(req,pk):
    customer = Customer.objects.get(cust_id=pk)
    user = User.objects.get(id = req.session['user'])
    print(req.session['user'])    
    # user = User.objects.get(id = customer.)
    if req.method == 'POST':
        print(req.POST)
        # form = UpdateCustomerForm(req.POST,instance=customer)
        # if form.is_valid():
        #     cus = Customer()
        #     cus.gender = req.POST.get('gender')
        #     cus.account = customer.account
        #     cus.save()
        #     form.save()    
        #     print('HIHI')
        #     return HttpResponseRedirect(reverse('home'))
        customer.firstname = req.POST.get('firstname')
        customer.lastname = req.POST.get('lastname')
        customer.age = req.POST.get('age')
        customer.gender = req.POST.get('gender')
        customer.tel = req.POST.get('tel')
        customer.address = req.POST.get('address')
        customer.account = user
        customer.save()
        return redirect('home')
    
    # form = UpdateCustomerForm(instance=customer)
    context = {
        # 'form':form,
        'customer':customer,
        'cusDate':str(customer.age),
    }
    print('FLASE')
    return render(req,'member/editcustomer.html',context)

@login_required
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


@login_required
def addrooms(req):
    if req.user.is_superuser:
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
    else:
        return redirect('home')

@login_required
def editrooms(req,pk):
    if req.user.is_superuser:
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
    else:
        return redirect('home')
@login_required
def editroom(req,pk,fk):
    if req.user.is_superuser:
        room = Rooms.objects.get(room_id = fk)
        if req.method == 'POST':
            form = Addroom(req.POST,instance=room)
            # form = AddRoomsClassForm(req.POST,instance=room)
            if form.is_valid():
                form.save()
                return redirect('editrooms',pk=pk)
        form = Addroom(instance=room)
        # form = AddRoomsClassForm(instance=room)
        context = {
            'form':form,
            'room':room
        }
        return render(req,'rooms/editroom.html',context)
    else:
        return redirect('home')
@login_required
def deleteroom(req,pk,fk):
    if req.user.is_superuser:
        room = Rooms.objects.get(room_id = pk)
        room.delete()
        # return HttpResponseRedirect(reverse('fetchrooms'))
        return redirect('editrooms',pk=fk)
    else:
        return redirect('home')
@login_required
def deletetype(req,pk):
    if req.user.is_superuser:
        type = RoomType.objects.get(type_id = pk)
        type.delete()
        rooms = Rooms.objects.all().filter(type_id = type)
        rooms.delete()
        return HttpResponseRedirect(reverse('fetchrooms'))
    else:
        return redirect('home')
@login_required
def addtype(req):
    if req.user.is_superuser:
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
    else:
        return redirect('home')
@login_required
def edittype(req,pk):
    if req.user.is_superuser:
        type = RoomType.objects.get(type_id = pk)
        multiimg = MultiImage.objects.all().filter(type = pk)
        
        if req.method == 'POST':
            form = AddRoomsTypeForm(req.POST,instance=type,files=req.FILES)
            images = req.FILES.getlist('image')
            # imgg = req.FILES.getlist('imggg')
            # print(imgg)
            print(form)
            if form.is_valid():
                typeForm = form.save()
                
                for i in images:
                    obj_img = MultiImage()
                    obj_img.image = i
                    obj_img.type = typeForm 
                    obj_img.save()

                return redirect('fetchrooms')
        else:
            form = AddRoomsTypeForm(instance=type)
            imgForm = MultiImageForm()
        context = {
            'imgForm':imgForm,
            'multiimg':multiimg,
            'form':form,
            'type':type
        }
        return render(req,'rooms/edittype.html',context)
    else:
        return redirect('home')
@login_required
def delMultiImg(req,id,type):
    if req.user.is_superuser:
        img = MultiImage.objects.get(id = id)
        img.delete()
        
        return redirect('edittype',pk=type)
    else:
        return redirect('home')
@login_required
def addanotherimg(req):
    if req.user.is_superuser:
        if req.method == 'POST':
            images = req.FILES.getlist('image')
            type = req.POST.get('type')
            room_type = RoomType.objects.get(type_id = type)
            for i in images:
                obj = MultiImage()
                obj.image = i
                obj.type = room_type
                obj.save()
        return redirect('edittype',pk=room_type.type_id)
    else:
        return redirect('home')
    
    
    
    
@login_required
def fetchrooms(req):
    if req.user.is_superuser:
        type = RoomType.objects.all()
        if req.method == 'POST':
            form = AddRoomsTypeForm(req.POST,req.FILES)
            imagess = req.FILES.getlist('image')
            print('file : ',req.FILES)
            print('adsasdsa',imagess)
            if form.is_valid():
                data = form.cleaned_data
                print(data)
                type_id = form.save()
                print(type_id)
                print(imagess)
                print('ok')
                for i in imagess:
                    print(i)
                    # MultiImage.objects.create(image = i,type=type_id)
                    obj_pro = MultiImage()
                    obj_pro.image = i
                    obj_pro.type = type_id
                    obj_pro.save()

                    print('upload success')
                    # MultiImage.objects.create(image = i,type=type_id)

                return HttpResponseRedirect(reverse('fetchrooms'))

        form = AddRoomsTypeForm()
        imgForm = MultiImageForm()
        context = {
            'type':type,
            'form':form,
            'imgForm':imgForm,
        }
        return render(req,'rooms/fetchrooms.html',context)
    else:
        return redirect('home')




def roomdetail(req,pk):
    typeCheck = RoomType.objects.get(type_id = pk)
    roomCheck = Rooms.objects.all().filter(type_id = pk,status = "ว่าง").count()
    multiimg = MultiImage.objects.all().filter(type = typeCheck)[:4]
    price = "{:,}".format(typeCheck.price)
    context = {
        'multiimg':multiimg,
        'price':price,
        'type':typeCheck,
        'count':roomCheck
    }
    return render(req,'rooms/roomdetail.html',context)


@login_required
def booking(req,pk):
    room_free = Rooms.objects.all().filter(type_id=pk,status = 'ว่าง').first()
    user = Customer.objects.get(account_id = req.session['user'])
    detail = RoomType.objects.get(type_id = pk)
    multiimg = MultiImage.objects.all().filter(type = pk)
    date_in = datetime.strptime(req.COOKIES['date_in'],'%Y-%m-%d').date()
    date_out = datetime.strptime(req.COOKIES['date_out'],'%Y-%m-%d').date()
    rental_day = date_out - date_in
    print(type(date_in))
    price = detail.price * rental_day.days
    remain_day = rental_day.days
    if req.method == 'POST':
        
        days = req.POST.get('days')
        sum_price = req.POST.get('sum_price')
        type_id = req.POST.get('type_id')
        room_id = req.POST.get('room_id')
         
        if req.POST.get('pay') == "later":
            trans = Transaction()
            trans.cust = user.account.username
            trans.room_id = room_id
            trans.roomtype = detail.name
            trans.status = "ยังไม่ชำระเงิน"
            trans.total = sum_price
            trans.save()
            book = Booking()
            book.date_in = date_in
            book.date_out = date_out
            book.total_payment = sum_price
            book.cust = user
            book.room = room_free
            book.transection = trans
            book_id = book.save()
            room_free.status = "ไม่ว่าง"
            room_free.save()
            return redirect('home')
        else:
            trans = Transaction()
            trans.cust = user.account.username
            trans.room_id = room_id
            trans.roomtype = detail.name
            trans.status = "ยังไม่ชำระเงิน"
            trans.total = sum_price
            trans.save()
            book = Booking()
            book.date_in = date_in
            book.date_out = date_out
            book.total_payment = sum_price
            book.cust = user
            book.room = room_free
            book.transection = trans
            book.save()
            room_free.status = "ไม่ว่าง"
            room_free.save()
            
            booking = Booking.objects.get(room_id = room_id)
            
            print('บันทึกสำเร็จ')
            form = PaymentForm()
            print(booking)
            context = {
                'room_free':room_free,
                'booking':booking,
                'form':form,
                'days':remain_day,
                'multiimg':multiimg,
            }   
            return redirect('bookingdetail',pk=book.booking_id)            
            # return render(req,'payment/payment.html',context)
        
    context = {
        'multiimg':multiimg,
        'room_free':room_free,
        'date_in':date_in,
        'date_out':date_out,
        'detail':detail,
        'days':remain_day,
        'price':price
    }
    return render(req,'booking/booking.html',context)

@login_required
def payment(req):
    if req.method == 'POST':
        user = Customer.objects.get(account_id = req.session['user'])
        pay_number = req.POST.get('pay_number')
        pay_expiry = req.POST.get('pay_expiry')
        pay_code = req.POST.get('pay_code')
        book_id = req.POST.get('booking_id')
        room_id = req.POST.get('room_free')
        select_book = Booking.objects.get(booking_id = book_id)
        print("trannnnnnnnnnnnn : ",select_book.transection.trans_id)
        transection = Transaction.objects.get(trans_id = select_book.transection.trans_id)
        
        pay = Payment()
        pay.pay_code = pay_code
        pay.pay_number = pay_number
        pay.pay_expiry = pay_expiry
        pay.cust = user
        pay.save()
        select_book.room.status = "ไม่ว่าง"
        select_book.status = "ชำระเงินเรียบร้อย"
        select_book.save()
        
        transection.status = "ชำระเงินเรียบร้อย"
        transection.save()
        # trans = Transaction()
        # trans.booking = select_book
        # trans.pay = pay
        # trans.cust = user
        # trans.save()

        print('ชำระเงินสำเร็จ')
        return redirect('bookingdetail',pk=book_id)

        
        
    return render(req,'payment/payment.html')
    
@login_required
def bookdetail(req,pk):
    
    booking = Booking.objects.get(booking_id = pk)
    
    date_in = booking.date_in    
    date_out = booking.date_out

    form = PaymentForm()
    multiimg = MultiImage.objects.all().filter(type = booking.room.type.type_id)[:4]
    remain_day = date_out.day - date_in.day
    
    
    context = {
        'multiimg':multiimg,
        'booking':booking,
        'remain_day':remain_day,
        'form':form
    }
    
    
    return render(req,'booking/bookdetail.html',context)
    
        
        
def alltype(req):
    alltype = RoomType.objects.all()
    
    context = {
        'alltype':alltype
    }
    return render(req,'rooms/alltype.html',context)                


def notFound(req,exception):
    response = render(req,'404page.html')
    response.status_code = 404
    return response

@login_required   
def transection(req):
    if req.user.is_superuser:

        info = Transaction.objects.all()
        all_total = Transaction.objects.all().aggregate(Sum('total')) 
        total = Transaction.objects.filter(status = "ชำระเงินเรียบร้อย").aggregate(Sum('total'))
        not_total = Transaction.objects.filter(status = "ยังไม่ชำระเงิน").aggregate(Sum('total'))
        cancle = Transaction.objects.filter(status = "ยกเลิกการจอง").aggregate(Sum('total'))
        count_paid = Transaction.objects.filter(status = "ชำระเงินเรียบร้อย").count()
        count_not = Transaction.objects.filter(status = "ยังไม่ชำระเงิน").count()
        count_cancle = Transaction.objects.filter(status = "ยกเลิกการจอง").count()
        val = list(total.values())    
        not_val = list(not_total.values())
        cancle_total = list(cancle.values())
        all = list(all_total.values())
        context = {
            'count_paid':count_paid,
            'count_not':count_not,
            'count_cancle':count_cancle,
            'cancle':cancle_total[0],
            'info':info,
            'total':val[0],
            'all':all[0],
            'not': 0 if not not_val[0] >= 0 else not_val[0],
            
        }
        
        return render(req,'transection.html',context)
    else:
        return redirect('home')
@login_required
def cancle(req,pk):

    booking = Booking.objects.get(booking_id = pk)
    room = Rooms.objects.get(room_id = booking.room_id)
    transection = Transaction.objects.get(trans_id = booking.transection.trans_id)

    booking.delete()
    room.status = "ว่าง"
    room.save()

    transection.status = "ยกเลิกการจอง"
    transection.save()
    
    return redirect('home')
    
def about(req):
    return render(req,'about.html')
    
def objective(req):
    return render(req,'objective.html')

def source(req):
    return render(req,'source.html')

@login_required   
def editmember(req):
    if req.user.is_superuser:

        member = Customer.objects.all()
        
        context = {
            'member':member,
        }
        
        return render(req,'member/editmember.html',context)
    else:
        return redirect('home')
@login_required
def editmember_admin(req,pk):
    if req.user.is_superuser:
        member = Customer.objects.get(cust_id=pk)
        # user = User.objects.get(id = req.session['user'])
        if req.method == 'POST':
            member.firstname = req.POST.get('firstname')
            member.lastname = req.POST.get('lastname')
            member.age = req.POST.get('age')
            member.gender = req.POST.get('gender')
            member.tel = req.POST.get('tel')
            member.address = req.POST.get('address')
            # member.account = user
            member.save()
            return redirect('editmember')
        
            
        else:
            memberForm = UpdateCustomerForm(instance = member)

        context = {
            'member':member,
            'memberForm':memberForm,
            'memDate':str(member.age),
        }
        return render(req,'member/editmember_admin.html',context)
    else:
        return redirect('home')
@login_required
def delmember_admin(req,pk):
    if req.user.is_superuser:
        member = User.objects.get(id = pk)
        member.delete()

        return redirect('editmember')
    else:
        return redirect('home')

