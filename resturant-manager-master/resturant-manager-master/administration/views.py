from django.shortcuts import redirect, render
from django.contrib import messages
from accounts.models import User
from accounts.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from accounts.forms import CreateUserForm, EditOrderForm, EditReservationForm, TableForm, TodaysSpecialForm, UserForm, FoodForm
from user.models import ContactUs, Food, FoodOrder, Order
from resturant.models import Reservation, Table, TodaysSpecial
from datetime import date,timedelta
# Create your views here.

def payment_stats():
    counter = Order.objects.filter(payment_type='1').count()
    online = Order.objects.filter(payment_type='2').count()
    if counter != 0 and online != 0:
        total = counter + online
        online_percentage = online/total*100
        counter_percentage = 100 - online_percentage
    else:
        if counter == 0:
            counter_percentage = 0
            online_percentage = 100
        elif online == 0:
            counter_percentage = 100
            online_percentage =0
    piechartdata = {
        'online':round(online_percentage),
        'counter':round(counter_percentage)
    }
    return piechartdata
def make_order_reservation_stats():
    today = date.today()
    yesterday = today - timedelta(1)
    two_days_ago = today - timedelta(2)
    three_days_ago = today - timedelta(3)
    four_days_ago = today - timedelta(4)
    five_days_ago = today - timedelta(5)
    six_days_ago = today - timedelta(6)

    order_today = Order.objects.filter(created_on=today).count()
    order_yesterday = Order.objects.filter(created_on=yesterday).count()
    order_two_days_ago= Order.objects.filter(created_on=two_days_ago).count()
    order_three_days_ago= Order.objects.filter(created_on=three_days_ago).count()
    order_four_days_ago= Order.objects.filter(created_on=four_days_ago).count()
    order_five_days_ago= Order.objects.filter(created_on=five_days_ago).count()
    order_six_days_ago= Order.objects.filter(created_on=six_days_ago).count()
    order_list = [order_six_days_ago,order_five_days_ago,order_four_days_ago,order_three_days_ago,order_two_days_ago,order_yesterday,order_today,0]

    reservation_today = Reservation.objects.filter(created_on=today).count()
    reservation_yesterday = Reservation.objects.filter(created_on=yesterday).count()
    reservation_two_days_ago= Reservation.objects.filter(created_on=two_days_ago).count()
    reservation_three_days_ago= Reservation.objects.filter(created_on=three_days_ago).count()
    reservation_four_days_ago= Reservation.objects.filter(created_on=four_days_ago).count()
    reservation_five_days_ago= Reservation.objects.filter(created_on=five_days_ago).count()
    reservation_six_days_ago= Reservation.objects.filter(created_on=six_days_ago).count()

    reservation_list = [reservation_six_days_ago,reservation_five_days_ago,reservation_four_days_ago,reservation_three_days_ago,reservation_two_days_ago,reservation_yesterday,reservation_today,0]
    output = {
        'order':order_list,
        'reservation':reservation_list
    }
    return output
    
@login_required
@allowed_users(allowed_roles=['admin'])
def admin_home(request):
    pie = payment_stats()
    order_reservation = make_order_reservation_stats()
    orders = Order.objects.filter(status='1')
    context = {
        'pie':pie,
        'orders':orders,
        'order_reservation':order_reservation
    }

    return render(request, 'administration/home.html',context)

"""
User Management Start
"""
@login_required
@allowed_users(allowed_roles=['admin'])
def admin_create_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'User {user.email} Created Successfully !', extra_tags="success")
            return redirect('admin_list_user')
        else:
            messages.error(request, 'Form Is Invalid Please Try Again !', extra_tags="error")    
    context = {'form':form}
    return render(request, 'administration/user/user_create.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_list_user(request):    
    user = User.objects.filter(is_admin=False)
    context = {'user':user}
    return render(request, 'administration/user/user_list.html' , context)

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_edit_user(request,pk):
    try:
        user = User.objects.get(id=pk)
    except:
        messages.error(request, 'Unable TO Fetch User', extra_tags="error")    
        return redirect('admin_list_user')
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'User {user.email} saved successfully !', extra_tags="success")
            return redirect('admin_list_user')
        else:
            messages.error(request, 'Form Is Invalid Please Try Again', extra_tags="error")    
    context = {
        'user':user,
        'form':form
    }
    return render(request, 'administration/user/user_edit.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_delete_user(request,pk):
    try:
        user = User.objects.get(id=pk)
    except:
        messages.error(request, 'Unable TO Fetch User', extra_tags="error")    
        return redirect('admin_list_user')
    if user:
        user.delete()
        messages.success(request, 'User Deleted Successfully !', extra_tags="success")   
    return redirect('admin_list_user')     

"""
User Management End
"""    

"""
Menu Management Start
"""
@login_required
@allowed_users(allowed_roles=['admin'])
def admin_list_menu(request):
    menu_starters = Food.objects.filter(category='1') 
    menu_main_dishes = Food.objects.filter(category='2') 
    menu_desserts = Food.objects.filter(category='3') 
    menu_drinks = Food.objects.filter(category='4') 
    menu_other = Food.objects.filter(category='5') 

    context = {
        'menu_starters':menu_starters,
        'menu_main_dishes':menu_main_dishes,
        'menu_desserts':menu_desserts,
        'menu_drinks':menu_drinks,
        'menu_other':menu_other
    }
    return render(request, 'administration/menu/menu_list.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_create_menu(request):
    form = FoodForm()
    if request.method == "POST":
        form = FoodForm(request.POST,request.FILES)
        if form.is_valid():
            food = form.save(commit=False)
            food.created_by = request.user
            food.save()
            messages.success(request, f'Food Item {food.name} Saved Successfully !', extra_tags="success")
            return redirect('admin_list_menu')
        else:
            messages.error(request, 'Form Is Invalid Please Check The Form !', extra_tags="error")   
    context = {
        'form':form
    }
    return render(request, 'administration/menu/menu_create.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_edit_menu(request,pk):
    try:
        food = Food.objects.get(id=pk)
    except:
        messages.error(request, 'Unable To Fetch Food Item !', extra_tags="error")    
        return redirect('admin_list_menu')
    form = FoodForm(instance=food)
    if request.method == "POST":
        form = FoodForm(request.POST,request.FILES,instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, f'Food Item - {food.name} saved successfully !',extra_tags="success")
            return redirect('admin_list_menu')
        else:
            messages.error(request, 'Form Invalid Please Check The Form !', )    
    context = {
        "food":food,
        "form":form
    }        
    return render(request, 'administration/menu/menu_edit.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_delete_menu(request,pk):
    try:
        food = Food.objects.get(id=pk)
    except:
        messages.error(request, 'Unable TO Fetch Food Item', extra_tags="error")    
        return redirect('admin_list_menu')
    if food:
        food.delete()
        messages.success(request, 'Food Item Deleted Successfully !', extra_tags="success")   
    return redirect('admin_list_menu')     
"""
Menu Management End
"""

"""
Todays Special Management Start
"""

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_list_todays_special(request):
    todays_special = TodaysSpecial.objects.all()
    context = {
        'todays_special':todays_special
    }
    return render(request, 'administration/todays_special/todays_special_list.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_create_todays_special(request):
    form = TodaysSpecialForm()
    if request.method == "POST":
        form = TodaysSpecialForm(request.POST, request.FILES)
        if form.is_valid():
            todays_special = form.save(commit=False)
            todays_special.created_by = request.user
            todays_special.save()
            messages.success(request, f"Today's Special {todays_special.name} added successfully !", extra_tags="success")
            return redirect('admin_list_todays_special')
        else:
            messages.error(request, 'Form Invalid Please Check The Form !', extra_tags="error")
    context = {"form":form}        
    return render(request, 'administration/todays_special/todays_special_create.html', context)            

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_edit_todays_special(request, pk):
    try:
        todays_special = TodaysSpecial.objects.get(id=pk)
    except:
        messages.error(request, "Unable To Fetch Today's Special Item !",extra_tags="error")    
        return redirect('admin_list_todays_special')
    form = TodaysSpecialForm(instance=todays_special)
    if request.method == "POST":
        form = TodaysSpecialForm(request.POST, request.FILES, instance=todays_special)
        if form.is_valid():
            todays_special = form.save(commit=False)
            messages.success(request, f"Today's Special {todays_special.name} saved successfully !", extra_tags="success")
            return redirect('admin_list_todays_special')
        else:
            messages.error(request, 'Form Invalid Please Check The Form !', extra_tags="error")
    context = {"form":form, 'todays_special':todays_special}        
    return render(request, 'administration/todays_special/todays_special_edit.html', context)            

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_delete_todays_special(request,pk):
    try:
        todays_special = TodaysSpecial.objects.get(id=pk)
    except:
        messages.error(request, 'Unable TO Fetch Todays Special Item !', extra_tags="error")    
        return redirect('admin_list_todays_special')
    if todays_special:
        todays_special.delete()
        messages.success(request, "Today's Special Deleted Successfully !", extra_tags="success")   
    return redirect('admin_list_todays_special')     

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_toggle_todays_special(request,pk):
    try:
        todays_special = TodaysSpecial.objects.get(id=pk)
    except:
        messages.error(request, 'Unable TO Fetch Todays Special Item !', extra_tags="error")    
        return redirect('admin_list_todays_special')
    if todays_special:
        if todays_special.is_active == True:
            todays_special.is_active = False
            todays_special.save()
            messages.success(request, "Today's Special Deactivated Successfully !", extra_tags="success")   
        else:
            todays_special.is_active = True
            todays_special.save()
            messages.success(request, "Today's Special Activated Successfully !", extra_tags="success")   
    return redirect('admin_list_todays_special')     

"""
Todays Special Management End
"""


"""
Table Management Start
"""
@login_required
@allowed_users(allowed_roles=['admin'])
def admin_list_table(request):
    tables = Table.objects.all()
    context = {
        'tables':tables
    }
    return render(request, 'administration/table/table_list.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_create_table(request):
    form = TableForm()
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            table = form.save()
            messages.success(request, f'Table #{table.number} added successfully !', extra_tags="success")
            return redirect('admin_list_table')
        else:
            messages.error(request, 'Form is Invalid Please Check the form !', extra_tags="error")    
    return render(request, 'administration/table/table_create.html',{'form':form})

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_edit_table(request,pk):
    try:
        table = Table.objects.get(id=pk)
    except:
        messages.error(request, 'Unable To Fetch Table !', extra_tags="error")    
        return redirect('admin_list_table')
    form = TableForm(instance=table)
    if request.method == "POST":
        form = TableForm(request.POST, instance=table)
        if form.is_valid():
            table = form.save()
            messages.success(request, f'Table #{table.number} saved successfully !', extra_tags="success")
            return redirect('admin_list_table')
        else:
            messages.error(request, 'Form is Invalid Please Check the form !', extra_tags="error")    

    return render(request, 'administration/table/table_edit.html',{'form':form,'table':table})    

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_delete_table(request,pk):
    try:
        table = Table.objects.get(id=pk)
    except:
        messages.error(request, 'Unable To Fetch Table', extra_tags="error")
    if table:
        table.delete()    
        messages.success(request ,'Successfully deleted table !', extra_tags="success")
    return redirect('admin_list_table')

"""
Table Management End
"""

"""
Reservation Management Start
"""
@login_required
@allowed_users(allowed_roles=['admin'])
def admin_list_reservation(request):
    reservation = Reservation.objects.all()
    context = {
        'reservation':reservation
    }
    return render(request, 'administration/reservation/reservation_list.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_edit_reservation(request,pk):
    try:
        reservation = Reservation.objects.get(id=pk)
    except:
        messages.error(request, 'Unable To Fetch Reservation with this id', extra_tags="error")    
    form = EditReservationForm(instance=reservation)    
    if request.method == "POST":
        form = EditReservationForm(request.POST,instance=reservation)    
        print(form)
        if form.is_valid():
            reservation = form.save()
            messages.success(request,f'Reservation #{reservation.id} Saved!', extra_tags="success")
            return redirect('admin_list_reservation')
        else:
            messages.error(request, 'Form Is Invalid Please Check The Form !', extra_tags="error")    
    context = {
        'form':form,
        'reservation':reservation
    }        
    return render(request, 'administration/reservation/reservation_edit.html',context)    

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_delete_reservation(request,pk):
    try:
        reservation = Reservation.objects.get(id=pk)
    except:
        messages.error(request, 'Unable To Fetch Reservation with this id', extra_tags="error")    
    if reservation:
        reservation.delete()    
        messages.success(request,'Reservation Deleted Successfully', extra_tags="success")
    else:
        messages.error(request, 'Unable to Delete Reservation', extra_tags="error")    
    return redirect('admin_list_reservation')    

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_detail_reservation(request,pk):
    try:
        reservation = Reservation.objects.get(id=pk)
    except:
        messages.error(request, 'Reservation not found !', extra_tags="error")  
    context = {'reservation':reservation}      
    return render(request, 'administration/reservation/reservation_detail.html',context)

"""
Reservation Management End
"""

"""
Order Start
"""
@login_required
@allowed_users(allowed_roles=['admin'])
def admin_list_order(request):
    order = Order.objects.all()
    return render(request, 'administration/order/order_list.html',{'order':order})

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_edit_order(request,pk):
    try:
        order = Order.objects.get(id=pk)
    except:
        messages.error(request, 'Unable To Fetch Order', extra_tags="error")    
    form = EditOrderForm(instance=order)    
    if request.method == "POST":
        form = EditOrderForm(request.POST,instance=order)
        if form.is_valid():
            order = form.save()
            messages.success(request,f'Order {order.id} saved successfully!', extra_tags="success")
            return redirect('admin_list_order')
        else:
            messages.error(request, 'Form Invalid Please Check The Form', extra_tags="error")
    context = {
        'form':form,
        'order':order
    }        
    return render(request, 'administration/order/order_edit.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_delete_order(request,pk):
    try:
        order = Order.objects.get(id=pk)
    except:
        messages.error(request, 'Unable To Fetch Order', extra_tags="error")    
    if order:
        order.delete()    
        messages.success(request, 'Successfully Deleted Order', extra_tags="success")
    else:
        messages.error(request, 'Unable to delete Order', extra_tags="error")    
    return redirect('admin_list_order')    

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_detail_order(request,pk):
    try:
        order = Order.objects.get(id=pk)
        food = FoodOrder.objects.filter(order=order)
    except:
        messages.error(request, 'Unable To Fetch Order', extra_tags="error")    
    context = {
        'order':order,
        'food':food
    }    
    return render(request, 'administration/order/order_detail.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_change_order_status(request,pk):
    try:
        order = Order.objects.get(id=pk)
    except:
        messages.error(request, 'Unable to Fetch Order', extra_tags="error")
    if order:
        if order.status == '1':
            order.status = '2'
            order.save()
            messages.success(request, f'Order #{order.id} set to completed',extra_tags="success")
        elif order.status == '2':
            order.status = '1'
            order.save()
            messages.success(request, f'Order #{order.id} set to placed', extra_tags="success")
        else:
            messages.error(request, 'Unable to change status', extra_tags="error")        
    else:
        messages.error(request, 'SYstem error Order Is not Defined', extra_tags="error")        
    return redirect('admin_home')    

"""
Order End
"""

"""
Contact Us
"""
@login_required
@allowed_users(allowed_roles=['admin'])
def admin_list_contact_us(request):
    contact_us = ContactUs.objects.all()
    return render(request, 'administration/contact_us/contact_us_list.html',{'contact_us':contact_us})

def admin_delete_contact_us(request,pk):
    try:
        contact_us = ContactUs.objects.get(id=pk)    
    except:
        messages.error(request, 'Unable To Fetch Contact US', extra_tags="error") 
    if contact_us:
        contact_us.delete()       
        messages.success(request, 'Successfully Deleted Contact Us', extra_tags="error")
    else:
        messages.error(request,'Unable to delete Contact Us', extra_tags="error")    
    return redirect('admin_list_contact_us')    
"""
Contact Us end
"""