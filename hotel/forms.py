from django import forms
from .models import *


GENDER_CHOICEs= [
    ('male','ชาย'),
    ('female','หญิง'),
]


class CustomerClassForm(forms.ModelForm):
    gender = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=GENDER_CHOICEs,
    )
    class Meta:
        model = Customer
        fields = ('name','age','gender','tel','address')
        labels = {
            'name':'ชื่อ',
            'age':'อายุ',
            'gender':'เพศ',
            'tel':'เบอร์โทร',
            'address':'ที่อยู่'
        }
        
class UpdateCustomerForm(forms.ModelForm):
    gender = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=GENDER_CHOICEs,
    )
    class Meta:
        model = Customer
        fields = ('cust_id','name','age','gender','tel','address')
        labels = {
            'name':'ชื่อ',
            'age':'อายุ',
            'gender':'เพศ',
            'tel':'เบอร์โทร',
            'address':'ที่อยู่'
        }



class AccountClassForm(forms.ModelForm):
    password = forms.CharField(max_length=60, required=True, label='Password',widget=forms.PasswordInput())
    class Meta:
        model = Accounts
        fields = ('username','password')
        labels = {
            'username':'Username',
            'password':'Password'
        }

    
    
class AddRoomsClassForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ('price','description','status','type')
        labels = {
            'price':'ราคา',
            'description':'รายละเอียด',
            'status':'สถานะ',
            'type':'ประเภท'
            
        }
    
class AddRoomsTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = ('name','description')
        labels = {
            'name':'ชื่อประเภท',
            'description':'รายละเอียดประเภทห้อง'
        }
    