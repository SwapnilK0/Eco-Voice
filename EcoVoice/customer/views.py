from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection, connections
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required

#Login signup and logout is remaining

# Create your views here.
 
def home(request):
    # return render(request,'home.html')
    return HttpResponse('Home Page for User')

def complaint(request):
    if request.method == 'POST':
        # data to write in the database
        # Here er use Ai model for image classification and store it in database
        print('complint')
    # return render(request,'complaint.html')
    return HttpResponse('File a Compliant here')



def ananomuscomplaint(request):
    if request.method == 'POST':
        # data to write in the database
        # Here er use Ai model for image classification and store it in database
       
        print('complint')
    
    return HttpResponse('File a Ananomus Compliant here') 
    # return render(request,'ananomuscomplaint.html')

def about_us(request):
    # return render(request,'about_us.html')
    return HttpResponse('here is about page') 

def blogs(request):
    if request.method == 'POST': # with Condition decorator
        #whenever a user is logged in then it can edit the blog
        print('blog')
    return HttpResponse('Blog Page')  
    # return render(request,'blogs.html')

def events(request):
    if request.method == 'POST': # with Condition decorator
        # data to write in the database
        # Here er use Ai model for image classification and store it in database
        print('Registration of event ')
    return HttpResponse('Event page')  
    # return render(request,'events.html')

# def upcoming_events(request): #it will include in event view
#     return render(request,'upcoming_events.html')


def events_registrations(request):
    # return render(request,'events_registrations.html')
    return HttpResponse('Event registration page')

def news(request):
    # return render(request,'news.html')
    return HttpResponse('News page')

def help(request):
    #it provide some of questions and answer 
    # return render(request,'help.html')
    return HttpResponse('help page')

def donation(request): # with Condition decorator
    if request.method == 'POST':
        # data to write in the database
        # Here er use donation logic
        
        print(donation)
       
    return HttpResponse('donation page')
    # return render(request,'donation.html')



#Condition decorator: I see. If you want to apply the login_required 
# decorator only to the post requests, but not to the get requests,
# you can use a conditional decorator. A conditional decorator is a function 
# that takes a view function and a condition as arguments, and returns either 
# the original view function or the decorated view function based on the condition
"""
def conditional_login_required(view_func, condition):
    def wrapper(request, *args, **kwargs):
        if condition(request):
            return login_required(view_func)(request, *args, **kwargs)
        else:
            return view_func(request, *args, **kwargs)
    return wrapper


def my_view(request):
    @conditional_login_required(lambda r: r.method == 'POST')
    def view(request):
        # handle both get and post requests
        ...
    return view(request)
"""