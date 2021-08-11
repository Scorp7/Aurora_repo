from django.contrib import admin
from .models import Reservation, TodaysSpecial

# Register your models here.

admin.site.register(Reservation)
admin.site.register(TodaysSpecial)