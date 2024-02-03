from django.contrib.auth.models import AbstractUser, Group , Permission
from django.db import models

class CustomCharityUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    # Additional fields for complaint filing
    charity_name = models.CharField(max_length=255, blank=True, null=True)
    charity_id = models.CharField(max_length=15, unique=True, blank=True, null=True)
    charity_address = models.TextField(blank=True, null=True)
    charity_city = models.CharField(max_length=20, blank=True, null=True)
    charity_state = models.CharField(max_length=20, blank=True, null=True)
    charity_zipcode = models.CharField(max_length=10, blank=True, null=True)
    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =['']
    groups = models.ManyToManyField(Group, related_name='charity_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='charity_user_permissions')

