from dataclasses import field
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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


# class DateInput(forms.DateInput):
#     input_type = 'date'

    


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
        self.fields['gender'].widget.attrs.update({'class':'form-control'})
        self.fields['tel'].widget.attrs.update({'class':'form-control'})
        self.fields['address'].widget.attrs.update({'class':'form-control'})
        
        
        
    gender = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=GENDER_CHOICEs,
    )
    class Meta:
        model = Customer
        fields = ('cust_id','firstname','lastname','age','gender','tel','address')
        labels = {
            'firstname':'ชื่อ',
            'lastname':'นามสกุล',
            'age':'อายุ',
            'gender':'เพศ',
            'tel':'เบอร์โทร',
            'address':'ที่อยู่'
        }

# class Login(forms.ModelForm):
#     def __init__(self,*args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update({'class':'form-control'})
#         self.fields['password'].widget.attrs.update({'class':'form-control'})

#     class Meta:
#         model = User
#         fields = ('username','password')
#         labels = {
#             'username':'Username',
#             'password':'Password'
#         }

# class AccountClassForm(forms.ModelForm):
#     password = forms.CharField(max_length=60, required=True, label='Password',widget=forms.PasswordInput(attrs={}))
#     confirm_password = forms.CharField(max_length=60, required=True, label='Confirm-password',widget=forms.PasswordInput(attrs={}))
#     def __init__(self,*args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update({'class':'form-control'})
#         self.fields['password'].widget.attrs.update({'class':'form-control'})
#         self.fields['confirm_password'].widget.attrs.update({'class':'form-control'})
#         self.fields['email'].widget.attrs.update({'class':'form-control'})
        
#     class Meta:
#         model = Accounts
#         fields = ('username','email','password','confirm_password')
#         labels = {
#             'username':'Username',
#             'password':'Password'
#         }
        
#     def clean(self):
#         cleaned_data = super().clean()
#         valpwd = self.cleaned_data['password']
#         valrpwd = self.cleaned_data['confirm_password']
#         if valpwd != valrpwd:
#             raise forms.ValidationError('Password does not match')

    
    
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
    limit_people = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=PEOPLE_CHOICES,label='จำนวนคนพัก')

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        self.fields['price'].widget.attrs.update({'class':'form-control'})
        self.fields['img'].widget.attrs.update({'class':'form-control'})
        self.fields['limit_people'].widget.attrs.update({'class':'form-control'})
    class Meta:
        model = RoomType
        fields = ('name','img','description','limit_people','price')
        labels = {
            'name':'ชื่อประเภท',
            'description':'รายละเอียดประเภทห้อง',
            'img':'รูปภาพ',
            'price':'ราคา',
            'limit_people':'จำนวนคนพัก'

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


class SearchForm(forms.ModelForm):
    people = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=PEOPLE_CHOICES)
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_in'].widget.attrs.update({'class':'form-control'})
        self.fields['date_out'].widget.attrs.update({'class':'form-control'})
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
              }),
            'date_out':forms.DateInput(
        format=('%d-%mm-%YYYYY'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
            
        }