from django import forms
from django.contrib.auth.forms import UserCreationForm
from resturant.models import Reservation, Table, TodaysSpecial
from user.models import ContactUs, Food, Order

from .models import User

"""
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['', '']
"""

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fname', 'lname', 'email', 'phone', 'profile_picture']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["fname", "lname", "email", "phone", "profile_picture"]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["fname", "lname", "email", "phone", "profile_picture", "is_active"]


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = ["order_count", "changed_on", "created_on", "created_by"]


class TodaysSpecialForm(forms.ModelForm):
    class Meta:
        model = TodaysSpecial
        exclude = ["created_on", "changed_on", "created_by", "is_active"]

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['user', 'created_on', 'changed_on', 'status']

class EditReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['created_on', 'changed_on']

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        exclude = ['created_on']        

class EditOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'user','reservation','accept_status','table','status','payment_type',
            'payment_is_complete','completed_on','amount' 
        ]

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ['created_on']        