from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import BaseUserManager, Group, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    """ Manager For User """
    def create_user(self, email, fname, lname,phone, password):
        """ Creates a new User """
        if not email:
            raise ValueError('Users must have an E-mail Address')
        email = self.normalize_email(email)
        user = self.model(email=email,fname=fname, lname=lname,phone=phone)
        user.set_password(password)
        print("Done")
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fname, lname,phone, password ):
        """ Creates a new Superuser """
        user = self.create_user(email, fname, lname,phone , password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        Group.objects.get_or_create(name='admin')
        group = Group.objects.get(name='admin')
        user.groups.add(group)
        user.save(using=self.db)
        return user
        
class User(AbstractBaseUser, PermissionsMixin):
    fname = models.CharField(max_length=100,blank=True,null=False)
    lname = models.CharField(max_length=100,blank=True,null=False)
    email = models.EmailField(max_length=100,blank=False,null=False,unique=True)
    phone = models.DecimalField(max_digits=10,blank=False,decimal_places=0,unique=True)
    profile_picture = models.ImageField(upload_to='profilepic/', blank=True, null=True)
    password = models.CharField(max_length=1000,blank=False,null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    changed_on = models.DateTimeField(auto_now=True,blank=False)
    created_on = models.DateTimeField(auto_now_add=True,blank=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname','phone']

    def __str__(self):
        return self.email # TODO