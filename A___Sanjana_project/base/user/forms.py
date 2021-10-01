from django import forms
from django.contrib.auth.models import User
from . import models

class UsersForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets = {
        'password': forms.PasswordInput(),
        }

