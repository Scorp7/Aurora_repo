from resturant.models import Reservation,Table
from django.db import models
from accounts.models import User
# Create your models here.

class Food(models.Model):
    category = (
        ('1', 'Starters'),
        ('2', 'Main Course'),
        ('3', 'Desserts'),
        ('4', 'Drinks'),
        ('5', 'Other')
    )
    name = models.CharField(max_length=100,blank=False)
    category = models.CharField(max_length=15,choices=category,blank=False,default='5')
    description = models.CharField(max_length=100,blank=False)
    price = models.DecimalField(max_digits=10,blank=False,decimal_places=0)
    image = models.ImageField(upload_to='food_images/',blank=True)
    order_count = models.IntegerField(blank=False, default=0)
    is_active = models.BooleanField(default=True,blank=False)
    changed_on = models.DateTimeField(blank=False,auto_now=True)
    created_on = models.DateTimeField(blank=False,auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    reservation = models.OneToOneField(Reservation, blank=True,on_delete=models.SET_NULL,null=True)
    placed_on = models.DateTimeField(blank=False,auto_now_add=True)
    accept_status = models.BooleanField(blank=True,default=True)
    status = (
        ('1', 'Placed'),
        ('2', 'Completed')
    )
    table = models.ForeignKey(Table,on_delete=models.DO_NOTHING,blank=True,null=True)
    status = models.CharField(blank=False,choices=status,max_length=10,default='1')
    payment_type = (
        ('0','Undefined'),
        ('1','Counter'),
        ('2','Online')
        )
    payment_type = models.CharField(blank=False,choices=payment_type,max_length=10,default='0')
    receipt_id = models.CharField(max_length=100,blank=True,null=True)
    order_id = models.CharField(max_length=100,blank=True,null=True)
    payment_id = models.CharField(max_length=100,blank=True,null=True)
    signature =models.CharField(max_length=100,blank=True,null=True)
    order_response = models.JSONField(blank=True,null=True)
    payment_response = models.JSONField(blank=True,null=True)
    payment_is_complete = models.BooleanField(blank=False,default=False)
    completed_on = models.DateTimeField(blank=True,null=True)
    food = models.ManyToManyField(Food,through='FoodOrder')
    amount = models.DecimalField(max_digits=10,decimal_places=0,blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True,blank=False)

    def __str__(self):
        return str(self.id) # TODO

class FoodOrder(models.Model):
    food = models.ForeignKey(Food,on_delete=models.CASCADE,blank=False)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,blank=False)
    quantity = models.IntegerField(blank=False,default=1)
    total = models.IntegerField(blank=False,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    changed_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.food.name) + " " + str(self.order.id)


class ContactUs(models.Model):
    email = models.EmailField(blank=False,max_length=255)
    message = models.CharField(max_length=1000,blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email + " - " + str(self.created_on)  # TODO

