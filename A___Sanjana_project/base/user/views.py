from django.shortcuts import render

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
    
