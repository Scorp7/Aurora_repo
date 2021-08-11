from django.contrib import admin
from .models import UserData

# Register your models here.
@admin.register(UserData)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email', 'gender', 'password')

