from django.contrib.auth import authenticate
from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib import messages

def authenticate_user(login_func):
    def wrapper(request, user=None):
        if request.user.is_authenticated:
            return HttpResponse('You have been Authenticated')
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                cd = login_form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        return login_func(request,user)
                    else:
                        messages.error(request, 'User is disabled')
                else:
                    messages.error(request, 'User does not exit')
            else:
                messages.error(request, 'Invalid username of passoword')
        else:
            login_form = LoginForm()
        return render(request, 'login.html', {'login_form': login_form})
    return wrapper
    