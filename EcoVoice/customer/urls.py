
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),#just for testing purposes at last delete it when project is done 
    path('', views.home, name='home'),
    # path('user_logout', views.user_logout, name='user_logout'),
    # path('user_login', views.user_login, name='user_login'),
    # path('user_signup', views.user_signup, name='user_signup'),

    path('home', views.home, name='home'),
    path('complaint', views.complaint, name='complaint'),   
    path('blogs', views.blogs, name='blogs'),
    path('about_us', views.about_us, name='about_us'),
    path('events', views.events, name='events'),
    # path('upcoming_events', views.upcoming_events, name='upcoming_events'),
    path('help', views.help, name='help'),
    path('donation', views.donation, name='donation'),
    
    
]
