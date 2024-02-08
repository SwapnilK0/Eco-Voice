from django.contrib import admin

# Register your models here.
from .models import  CustomCharityUser,Event,Blog,Donation

admin.site.register( CustomCharityUser)
admin.site.register(Event)
admin.site.register(Blog)
admin.site.register(Donation)