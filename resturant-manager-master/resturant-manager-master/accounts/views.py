from django.shortcuts import redirect, render
from django.contrib import auth
# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('authenticate')