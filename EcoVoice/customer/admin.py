from django.contrib import admin

# Register your models here.
from .models import CustomUser, Complaint

admin.site.register(CustomUser)
admin.site.register(Complaint)