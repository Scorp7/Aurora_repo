from django import contrib
from accounts.forms import ContactUsForm, ProfileEditForm, ReservationForm
import hmac
import hashlib
from resturant.models import Reservation, TodaysSpecial
from django.contrib import messages
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt
from accounts.models import User
from .models import Food, FoodOrder, Order, Table
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from base.settings import DOMAIN, RAZORPAY_CLIENT, RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET
from django.contrib.auth.hashers import make_password
from accounts.decorators import admin_not_allowed, unauthenticated_user
# Create your views here.
@admin_not_allowed
def home(request):
    starters = Food.objects.filter(category='1', is_active=True)
    main_dishes = Food.objects.filter(category='2', is_active=True)
    desserts = Food.objects.filter(category='3', is_active=True)
    drinks = Food.objects.filter(category='4', is_active=True)
    other = Food.objects.filter(category='5', is_active=True)
    menu = {
        'starters':starters,
        'main_dishes':main_dishes,
        'desserts':desserts,
        'drinks':drinks,
        'other':other
    }
    todays_special = TodaysSpecial.objects.filter(is_active=True)
    new_reservationform = ReservationForm()
    context = {
        'domain':DOMAIN,
        'menu':menu,
        'todays_special':todays_special,
        'new_reservationform':new_reservationform
    }
    return render(request, 'user/home.html',context)

def reservation_backend(request):
    reservation = None
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        email = request.POST.get('email')
        print(form)
        if form.is_valid():
            if email:
                user = User.objects.filter(email=email)
                if user:
                    try:
                        user = User.objects.get(email=email)
                        is_user = True
                    except:
                        messages.error(request, 'Unable To Fetch User With This Email', extra_tags="error")    
                else:
                    is_user = None
                if is_user and user:
                    reservation = form.save()    
                    reservation.user = user
                    reservation.save()
                else:
                    reservation = form.save()
                    messages.success(request,'Successfully Reserved', extra_tags="success")    
                people = reservation.number_of_persons
                tables = Table.objects.filter(is_occupied=False,status=True)
                print(tables)
                if tables:
                    for table in tables:
                        print('baba')
                        if table.capacity == people:
                                selected_table = table
                                break
                        elif table.capacity > people:
                                selected_table = table
                                break
                        else:
                                selected_table = None
                    print(selected_table)
                    if selected_table:
                        reservation.table = selected_table
                        selected_table.is_occupied = True
                        reservation.save()
                        selected_table.save()
                    messages.success(request, f'Successfully Reserved Table #{selected_table.number}', extra_tags="success")
            else:
                messages.error(request, 'Email Is Required !', extra_tags="error")        
        else:
            messages.error(request,'Form Invalid Please Check The Form')
    else:
        messages.error(request, 'Only Post requests allowed at this endpoint')    
    return redirect('home')    

@admin_not_allowed
@unauthenticated_user
def authenticate(request):
    return render(request, 'user/login.html',{'domain' : DOMAIN})    

#@unauthenticated_user
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email)
        if not user:
            messages.error(request, 'Email Not Registered !', extra_tags="error")
            return redirect('authenticate')
        else:
            user = auth.authenticate(username=email,password=password)
            if user:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid Credentials !', extra_tags="error")
                return redirect('authenticate')
    else:
        messages.error(request, 'Only Post Requests Are Allowed On This Endpoint', extra_tags="error")
    return redirect('authenticate')            

def register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        check = User.objects.filter(email=email)
        if check:
            messages.error(request, 'Email Address Already registered!', extra_tags="error")
            return redirect('authenticate')
        phone = request.POST.get('phone')
        check = User.objects.filter(phone=phone)
        if check:
            messages.error(request, 'User with this phone number already exists!', extra_tags="error")
            return redirect('authenticate')    
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if fname and lname and email and phone and password1 and password2:
            if password1 == password2:
                user = User.objects.create(fname=fname,lname=lname,email=email,phone=phone,password=make_password(password1))    
                group = Group.objects.get_or_create(name="customer")
                user.groups.add(group[0])
                user.save()
                if user:
                    messages.success(request, 'Successfully Registered You Can Login Now !', extra_tags="success")
                else:
                    messages.error(request, 'Unable To Create User', extra_tags="error")
            else:
                messages.error(request, 'Passwords Do Not Match !', extra_tags="error")
        else:
            messages.error(request, 'Form Incomplete Please Check The Form', extra_tags="error")                
    else:
        messages.error(request, 'Only Post Requests Are Allowed On This Endpoint', extra_tags="error")
    return redirect('authenticate')            

@admin_not_allowed
@login_required
def user(request,pk):
    profile_edit_form = ProfileEditForm(instance=request.user)
    orders = Order.objects.filter(user=request.user)
    reservations = Reservation.objects.filter(user=request.user)
    food_order = None
    for order in orders:
        food = FoodOrder.objects.filter(order=order)
        if food_order:
            food_order = food_order | food
        else:
            food_order = food   
    
    if request.method == "POST":
        profile_edit_form = ProfileEditForm(request.POST,request.FILES,instance=request.user)
        if profile_edit_form.is_valid():
            profile_edit_form.save()
            messages.success(request, 'Profile Changed Successfully', extra_tags="success")
            return redirect('user',pk=request.user.email)
        else:
            messages.error(request, 'Form Invalid Please Check The Form', extra_tags="error")    
    context = {
        'domain':DOMAIN,
        'form':profile_edit_form,
        'orders':orders,
        'food_order':food_order,
        'reservations':reservations
        }
    return render(request, 'user/user.html',context)

@admin_not_allowed
def order(request):
    price = user_has_reserved = 0
    if not request.user.is_authenticated:
        messages.error(request, 'Please Login/Register To Order', extra_tags="error")
        return redirect('authenticate')
    food = Food.objects.filter(is_active=True)
    table = Table.objects.filter(is_occupied=False,status=True)
    if Reservation.objects.filter(user=request.user,is_expired=False):
        user_has_reserved = True
    if request.method == "POST":
        order = Order.objects.create(user=request.user)
        if not user_has_reserved:
            if not request.POST.get('table'):
                print(request.POST)
                messages.error(request,'Please Select Table', extra_tags="error")
                return redirect('order')
        loop_count = 0
        selected_table = request.POST.get('table')
        if user_has_reserved:    
            reservation = Reservation.objects.get_or_create(user=request.user,is_expired=False)
            if reservation:
                selected_table = reservation[0].table 
                reservation[0].order = order
                reservation[0].status = 'reserved'
                reservation[0].is_expired = True
                reservation[0].save()
        else:        
            try:
                selected_table = Table.objects.get(id=selected_table)
            except:
                messages.error(request, 'Unable to assign that table', extra_tags="error")
        if selected_table:
            order.table = selected_table
        for i in request.POST:
            if i.isnumeric():
                item_qty = int(request.POST.get(i))
                if item_qty > 0:
                    try:
                        food_item = Food.objects.get(id=i)
                    except:
                        print("error: Unable To Fetch Food Item")
                    if food_item and item_qty:   
                        item_price = food_item.price * item_qty 
                        price = price + item_price
                        food_order = FoodOrder.objects.create(order=order,food=food_item,quantity=item_qty,total=item_price)
                        if food_order:
                            food_item.order_count = food_item.order_count + 1
                            food_item.save()     
        order.amount = price                
        if Reservation.objects.filter(user=request.user,is_expired=False):
           reservation = Reservation.objects.get_or_create(user=request.user,is_expired=False) 
           order.reservation = reservation[0]
           order.table = reservation[0].table
        order.save()
        return redirect('order_confirmation', pk=order.id)
    context = {
        'domain':DOMAIN,
        'foods':food,
        'table':table,
        'user_has_reserved':user_has_reserved
        }    
    return render(request, 'user/order.html', context)

@admin_not_allowed
@login_required
def order_confirmation(request,pk):
    try:
        order = Order.objects.get(id=pk)
        food_order = FoodOrder.objects.filter(order=order)
        print(food_order)
    except:
        messages.error(request,'Unable TO Fetch Order', extra_tags="error")        
    if not order.user == request.user:    
        messages.error(request,'Please Login To check details of order', extra_tags="error")
        return redirect('home')
    if request.method == "POST":
        payment_type = request.POST.get('payment_type')    
        if payment_type == 'counter':
            order.payment_type = '1'
            order.save()
            messages.success(request, 'You Have Selected Pay On Counter As Payment Option',extra_tags="success")
            return redirect('user', pk=request.user.email)
        elif payment_type == 'online':
            order.payment_type = '2'
            order.save()
            amt = str(order.amount) + "00"
            receipt_id = "#"+ str(order.id) + f"-{amt}"
            response = RAZORPAY_CLIENT.order.create(dict(amount=amt, currency="INR", receipt=receipt_id))        
            if response and response['status'] == 'created':
                response_json = response
                order.order_response = response_json
                order.order_id = response['id']
                order.receipt_id = response['receipt']
                order.save()
                return redirect('order_payment',pk=order.id)
        else:
            messages.error(request, 'Unable to fetch payment method', extra_tags="error")
            
    context = {
        'domain':DOMAIN,
        'order':order,
        'food_order':food_order
    }    
    return render(request, 'user/order_confirmation.html', context)

def order_payment(request,pk):

    try:
        order = Order.objects.get(id=pk)
        food_order = FoodOrder.objects.filter(order=order)
        print(food_order)
    except:
        messages.error(request,'Unable TO Fetch Order', extra_tags="error")        
    context = {
        'domain':DOMAIN,
        'order':order,
        'razorpay_key_id':RAZORPAY_KEY_ID,
    }    
    return render(request,'user/order_payment.html',context )

@csrf_exempt
def payment_success(request,pk):
    try:
        order = Order.objects.get(id=pk)
    except:
        messages.error(request,'Unable TO Fetch Order', extra_tags="error")        
    if request.method == "POST":
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_signature = request.POST.get('razorpay_signature')
        if order.order_id == razorpay_order_id:
            a = f"{order.order_id}|{razorpay_payment_id}"
            secret = bytes(RAZORPAY_KEY_SECRET,'utf-8')
            a = bytes(a, 'utf-8')
            b = hmac.new(secret,a,hashlib.sha256) 
            generated_signature = b.hexdigest()
            if generated_signature == razorpay_signature: 
                order.payment_response = dict({
                    'payment_id':razorpay_payment_id,
                    'order_id':razorpay_order_id,
                    'signature': razorpay_signature,
                })
                order.payment_id = razorpay_payment_id
                order.signature = razorpay_signature
                order.payment_is_complete = True
                order.save()
                messages.success(request, 'Payment Successful', extra_tags="success")
                return redirect('user',pk=request.user.email)
            else:
                messages.error(request, 'Generated Signature Does Not Match',extra_tags="error")    
    return redirect('home')            

def contact_us_backend(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()    
            messages.success(request, 'Message Sent Successfully!', extra_tags="success")
        else:
            messages.error(request, 'Form Invalid Please Check The Form!' ,extra_tags="error")    
    else:
        messages.error(request,'Only get allowed on this endpoint',extra_tags="error")        

    return redirect('home')
