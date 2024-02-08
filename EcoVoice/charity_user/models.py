from django.contrib.auth.models import AbstractUser, Group , Permission
from django.db import models

class CustomCharityUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    # Additional fields for complaint filing
    charity_name = models.CharField(max_length=255)
    charity_id = models.CharField(max_length=15, unique=True)
    charity_address = models.TextField(max_length=100)
    charity_city = models.CharField(max_length=20)
    charity_state = models.CharField(max_length=20)
    charity_zipcode = models.CharField(max_length=10)
    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =['']
    groups = models.ManyToManyField(Group, related_name='charity_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='charity_user_permissions')


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_id = models.IntegerField(unique=True)
    event_address = models.CharField(max_length=100)
    event_city = models.CharField(max_length=100)
    event_state = models.CharField(max_length=100)
    #   event_type = models.CharField(max_length=100)
    event_host = models.CharField(max_length=100)
    event_date = models.DateField(auto_now=False, auto_now_add=False)
    
    
class Blog(models.Model):
    
    authour_name = models.CharField(max_length=100)
    # + blog_type : text
    blog_heading = models.CharField(max_length=100)
    blog_discreption = models.TextField()
    uploded_date = models.DateField(auto_now=False, auto_now_add=False)
    
class Donation(models.Model):
    donation_id =  models.CharField(max_length=100)
    donaor =  models.CharField(max_length=100)
    beneficiary = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    trancaction_method= models.CharField(max_length=100)



