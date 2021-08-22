from django.contrib import admin
from .models import UserData, User

# Register your models here.
@admin.register(UserData)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email', 'gender', 'password')

admin.site.register(User)