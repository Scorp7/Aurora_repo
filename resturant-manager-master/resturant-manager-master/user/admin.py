from django.contrib import admin
from .models import ContactUs, Order, Food, Table, FoodOrder
# Register your models here.
admin.site.register(Order)
admin.site.register(Food)
admin.site.register(FoodOrder)
admin.site.register(Table)
admin.site.register(ContactUs)
