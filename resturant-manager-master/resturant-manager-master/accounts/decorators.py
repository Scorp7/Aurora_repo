from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.http import HttpResponse

def admin_not_allowed(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.filter(name__in=["admin"]).exists():
                return redirect("admin_home")
            elif request.user.is_admin:
                return redirect("admin_home")        
            else:
                return view_func(request, *args, **kwargs)
        else:
                return view_func(request, *args, **kwargs)        
    return wrapper_func


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.filter(name__in=["admin"]).exists():
                return redirect("admin_home")
            elif request.user.groups.filter(name__in=["customer"]).exists():
                return redirect("home")
            else:
                user = request.user
                group = Group.objects.get_or_create(name="customer")
                group = group[0]
                user.groups.add(group)
                user.save()
                return HttpResponse('System Misconfiguration trying automatic repair....')
                
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return render(request, "unauthorised.html")

        return wrapper_func

    return decorator
