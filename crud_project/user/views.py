from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .forms import UserRegistration
from .models import UserData


# This is test function
def test_data(request):
    return render(request, 'user/test.html')


#This function will add new item and show all items
def add_show(request):

    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            ag = form.cleaned_data['age']
            em = form.cleaned_data['email']
            gndr = form.cleaned_data['gender']
            pw = form.cleaned_data['password']
            all_ = UserData(name=nm, age=ag, email=em, gender=gndr, password=pw)
            all_.save()
            form = UserRegistration()
    else:
        form = UserRegistration()
    data = UserData.objects.all()
    

    return render(request, 'user/ad_show.html', {'Form': form, 'Data': data})


#This funciton will delete
def delete_data(request, id):
    if request.method == "POST":
        pi = UserData.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/user/')


#This function will Edit
def edit_data(request, id):
    pi = UserData.objects.get(pk=id)
    form = UserRegistration(instance=pi)
    if request.method == "POST":
        form = UserRegistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
        else:
            pi = UserData.objects.get(pk=id)
            form = UserRegistration(instance=pi)
    return render (request, 'user/edit.html', {'Form': form})


