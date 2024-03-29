
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from datetime import datetime,date 



GENDER_CHOICEs= [
    ('male','ชาย'),
    ('female','หญิง'),
]

STATUS_CHOICES= [
    ('ว่าง','ว่าง'),
    ('ไม่ว่าง','ไม่ว่าง')
]

PEOPLE_CHOICES = [
    (1,'1 คน'),
    (2,'2 คน'),
    (4,'2-4 คน'),
]

BED_CHOICES = [
    ('1 เตียงเดี่ยว','1 เตียงเดี่ยว'),
    ('2 เตียงคู่','2 เตียงคู่')
]




class CustomerClassForm(forms.ModelForm):
    gender = forms.ChoiceField(required=True,widget=forms.RadioSelect(attrs={}),choices=GENDER_CHOICEs,)
   
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['firstname'].widget.attrs.update({'class':'form-control'})
        self.fields['lastname'].widget.attrs.update({'class':'form-control' })
        self.fields['age'].widget.attrs.update({'class':'form-control'})
        self.fields['gender'].widget.attrs.update({'class':''})
        self.fields['tel'].widget.attrs.update({'class':'form-control'})
        self.fields['address'].widget.attrs.update({'class':'form-control'})
        
   
    class Meta:
        model = Customer
        fields = ('firstname','lastname','age','gender','tel','address')
        widgets = {
            'age':forms.DateInput(
        format=('%dd-%mm-%Y'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
            
        }
        labels = {
            'firstname':'ชื่อ',
            'lastname':'นามสกุล',
            'age':'อายุ',
            'gender':'เพศ',
            'tel':'เบอร์โทร',
            'address':'ที่อยู่'
        }

  



class RegisterForm(UserCreationForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        self.fields['password1'].widget.attrs.update({'class':'form-control'})
        self.fields['password2'].widget.attrs.update({'class':'form-control'})

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
       



        
class UpdateCustomerForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['firstname'].widget.attrs.update({'class':'form-control'})
        self.fields['lastname'].widget.attrs.update({'class':'form-control'})
        self.fields['age'].widget.attrs.update({'class':'form-control'})
        self.fields['tel'].widget.attrs.update({'class':'form-control'})
        self.fields['address'].widget.attrs.update({'class':'form-control'})
        
        
        
    gender = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=GENDER_CHOICEs,
    )
    class Meta:
        model = Customer
        fields = ('cust_id','firstname','lastname','age','tel','address')
        labels = {
            'firstname':'ชื่อ',
            'lastname':'นามสกุล',
            'age':'อายุ',
            'gender':'เพศ',
            'tel':'เบอร์โทร',
            'address':'ที่อยู่'
        }



    
    
class AddRoomsClassForm(forms.ModelForm):
    status = forms.ChoiceField(
        required=True,
        widget=forms.Select,
        choices=STATUS_CHOICES,
    )
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        self.fields['status'].widget.attrs.update({'class':'form-control'})
        self.fields['type'].widget.attrs.update({'class':'form-control'})
    class Meta:
        model = Rooms
        fields = ('description','status','type')

        labels = {

            'description':'รายละเอียด',
            'status':'สถานะ',
            'type':'ประเภท'
            
        }
    
class AddRoomsTypeForm(forms.ModelForm):
    bed = forms.ChoiceField(
        required=True,
        widget=forms.Select,
        choices=BED_CHOICES,
        label="จำนวนเตียง",
    )
    limit_people = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=PEOPLE_CHOICES,label='จำนวนคนพัก')
    img = forms.ImageField(widget=forms.FileInput)
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        self.fields['price'].widget.attrs.update({'class':'form-control'})
        self.fields['img'].widget.attrs.update({'class':'form-control'})
        self.fields['limit_people'].widget.attrs.update({'class':'form-control'})
        self.fields['bed'].widget.attrs.update({'class':'form-control'})
    class Meta:
        model = RoomType
        fields = ('name','img','description','limit_people','price','bed')
        labels = {
            'name':'ชื่อประเภท',
            'description':'รายละเอียดประเภทห้อง',
            'img':'รูปภาพ',
            'price':'ราคา',
            'limit_people':'จำนวนคนพัก',
            'bed':'จำนวนเตียง',

        }
    
    
class Addroom(forms.ModelForm):
    status = forms.ChoiceField(
        required=True,
        widget=forms.Select,
        choices=STATUS_CHOICES,
    )
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        self.fields['status'].widget.attrs.update({'class':'form-control'})
    class Meta:
        model = Rooms
        fields = ('description','status')
        labels = {
            'description':'รายละเอียด',
            'status':'สถานะ',            
        }
        
        
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date_in','date_out')
        labels = {
            'date_in':'วันที่เข้า',
            'date_out':'วันที่ออก'
        }
        widgets = {
            'date_in':forms.DateInput(
        format=('%d-%mm-%YYYY'),
        attrs={'class': 'form-control', 
               'placeholder': '',
               'type': 'date'
              }),
            'date_out':forms.DateInput(
        format=('%d-%mm-%YYYYY'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
            
        }

def mydate():
    return str(date.today())

class SearchForm(forms.ModelForm):
    people = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=PEOPLE_CHOICES)
    
    def __init__(self,*args, **kwargs):
        self.check_in = kwargs.pop('check_in', None)
        self.check_out = kwargs.pop('check_out', None)
        super().__init__(*args, **kwargs)
        
        self.fields['date_in'].widget.attrs.update({'class':'form-control','min':str(date.today()),'value':self.check_in})
        self.fields['date_out'].widget.attrs.update({'class':'form-control','min':str(date.today()),'value':self.check_out})
    class Meta:
        model = Booking
        fields = ('date_in','date_out','people')
        labels = {
            'date_in':'วันที่เข้า',
            'date_out':'วันที่ออก',
            
        }
        widgets = {
            'date_in':forms.DateInput(
        format=('%d-%mm-%YYYY'),
        attrs={'class': 'form-control', 
               'placeholder': '',
               'type': 'date'
              }
        ),
            'date_out':forms.DateInput(
        format=('%d-%mm-%YYYYY'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),            
        }
        
class MultiImageForm(forms.ModelForm):
    image = forms.ImageField(
        label='รูปภาพเพิ่มเติม',
        widget=forms.ClearableFileInput(attrs={"multiple":True,"class":"form-control","id":"imagex"}),
    )
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
    class Meta:
        model = MultiImage
        fields = ('image',)        
        
class PaymentForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pay_number'].widget.attrs.update({'class':'form-control'})
        self.fields['pay_expiry'].widget.attrs.update({'class':'form-control'})
        self.fields['pay_code'].widget.attrs.update({'class':'form-control'})
    class Meta:
        model = Payment
        fields = ('pay_number','pay_expiry','pay_code')
        labels = {
            'pay_number':'รหัสบัตร',
            'pay_expiry':'วันหมดอายุ',
            'pay_code':'รหัสความปลอดภัย'
        }
        
