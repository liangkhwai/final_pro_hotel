from pyexpat import model
from django import forms
from .models import hotel


class regisForm(forms.ModelForm):
    class Meta:
        model = hotel
        exc


