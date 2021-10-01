from django.shortcuts import render
from . import forms,models
# Create your views here.
def index(request):
    return render(request,'user/index.html')
    
def about(request):
    return render(request,'user/about.html')
    
def cart(request):
    return render(request,'user/cart.html')

def contactus(request):
    return render(request,'user/contactus.html')
    
def desserts(request):
    return render(request,'user/desserts.html')
    
def mutton(request):
    return render(request,'user/mutton.html')

def chicken(request):
    return render(request,'user/chicken.html')
    
def nonvegsoup(request):
    return render(request,'user/nonvegsoup.html')
    
def nonvegstarter(request):
    return render(request,'user/nonvegstarter.html')

def order(request):
    return render(request,'user/order.html')
    
def payment(request):
    return render(request,'user/payment.html')
    
def rice(request):
    return render(request,'user/rice.html')

def roti(request):
    return render(request,'user/roti.html')
    
def seafood(request):
    return render(request,'user/seafood.html')
    
def vegetariandishes(request):
    return render(request,'user/vegetariandishes.html')
    
def starter(request):
    return render(request,'user/starter.html')
    
def vegsoups(request):
    return render(request,'user/vegsoups.html')
    
def user_signup(request):
    userForm=forms.UsersForm()
    mydict={'userForm':userForm}
    if request.method=='POST':
        userForm=forms.UsersForm(request.POST)
        if userForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
        return render(request,'user/login.html')
    return render(request,'user/signup.html',context=mydict)


# def is_student(user):
#     return user.groups.filter(name='STUDENT').exists()

def login(request):
    return render(request,'user/login.html')
    