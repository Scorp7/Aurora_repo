from django.db import models
from accounts.models import User
# Create your models here.

class Table(models.Model):
    number = models.IntegerField(blank=False)
    capacity = models.IntegerField(blank=False)
    status = models.BooleanField(blank=False, default=False)
    is_occupied = models.BooleanField(default=False,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"#{self.number} ({self.capacity} Persons)"  # TODO

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True,null=True)
    name = models.CharField(max_length=255,blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    phone = models.DecimalField(max_digits=10,decimal_places=0,blank=False)
    n = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10),
    )
    number_of_persons = models.IntegerField(choices=n,blank=False)
    date = models.CharField(max_length=100,blank=False,null=False,default="May 5")
    time = models.CharField(blank=False,max_length=100)
    food = (
        ('indian', 'INDIAN'),
        ('chinese', 'CHINESE'),     
        ('italian', 'ITALIAN'),
        ('thai', 'THAI'),           
        ('no_pref', 'NO PREFERENCE')
    )
    preferred_food = models.CharField(choices=food, max_length=100,blank=True)
    occation = (
        ('birthday', 'Birthday'),
        ('wedding', 'Wedding'),
        ('anniversary', 'Anniversary'),
        ('casual', 'Casual')
    )
    occation = models.CharField(choices=occation,blank=True,max_length=100)
    table = models.ForeignKey(Table, on_delete=models.DO_NOTHING,blank=True,null=True)
    status = (
        ('reserved','Reserved'),
        ('unreserved','Unreserved'),
        ('undefined','Undefined')
    )
    is_expired = models.BooleanField(blank=False,default=False)
    status = models.CharField(choices=status,blank=True,max_length=10,default='undefined') 
    created_on = models.DateTimeField(auto_now_add=True,blank=False)
    changed_on = models.DateTimeField(auto_now=True,blank=False)

    def __str__(self):
        return str(self.email) + "-" + str(self.created_on) # TODO

class TodaysSpecial(models.Model):
    name = models.CharField(max_length=20,blank=False)
    description = models.CharField(max_length=100,blank=False) 
    image = models.ImageField(upload_to='todays_special/',blank=False)
    is_active = models.BooleanField(default=True, blank=False)
    created_on = models.DateField(auto_now_add=True,blank=False)
    changed_on = models.DateField(auto_now=True,blank=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name # TODO      