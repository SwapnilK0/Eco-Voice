from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    # Additional fields for complaint filing
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =['email']
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')


class Complaint(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    complint_name = models.CharField(max_length=100, blank=True, null=True)
    crime_type = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.IntegerField()
    crime_date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    


