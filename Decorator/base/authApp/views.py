from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from .decorators import authenticate_user

def register_view(request):
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
    else:
        register_form = UserCreationForm()
    return render(request, 'register.html', {'register_form': register_form})
    
@authenticate_user
def login_view(request, user=None):
    login(request, user)
    return HttpResponse('{} you have logged in successfully'.format(request.user))  