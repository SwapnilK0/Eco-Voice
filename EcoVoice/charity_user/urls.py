
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),#it is different from basic home
    # path('user_logout', views.user_logout, name='user_logout'), #charity login
    # path('user_login', views.user_login, name='user_login'), #charity logout
    # path('user_signup', views.user_signup, name='user_signup'), #charity signup wiyh validation
    path('create_charity_user', views.create_charity_user, name='create_charity_user'),
    path('home', views.home, name='home'), #it is different from basic home 
    path('complaint', views.complaint, name='complaint'),  #Show the all compliant
    path('ananomuscomplaint', views.ananomuscomplaint, name='ananomuscomplaint'),  #Show the all ananomus compliant
    path('blogs', views.blogs, name='blogs'),#edit te blog here
    path('about_us', views.about_us, name='about_us'), #blog will same 
    path('events', views.events, name='events'),#add event and its discription
    # path('upcoming_events', views.upcoming_events, name='upcoming_events'),#Add events
    path('help', views.help, name='help'),#in this we show help for how to use website
    path('donation_details', views.donation_details, name='donation_details'), #in this we show the total donation collected
    
    
]
