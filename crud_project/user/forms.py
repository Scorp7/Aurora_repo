from django.core import validators
from django import forms
from django.forms import widgets
from django.forms.models import ModelForm
from .models import UserData

class UserRegistration(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ["name", "age", "email", "gender", "password"]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'age': forms.NumberInput(attrs={'class':'form-control','id':'ageid'}),
            'email': forms.EmailInput(attrs={'class':'form-control','id':'emailid'}),
            # 'gender': forms.TextInput(attrs={'class':'custom-select mr-sm-2'}),
            'password': forms.PasswordInput(render_value=True ,attrs={'class':'form-control','id':'passwordid'}),
        }
