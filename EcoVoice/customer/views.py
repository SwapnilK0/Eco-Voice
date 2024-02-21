from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from customer.models import *
from charity_user.views import create_blog
from charity_user.models import *
from charity_user.utils import * 
from .manager import *
import uuid

#Login signup and logout is remaining

def user_login(request) :
    if request.method == 'POST':

        email= request.POST.get('email')
        password= request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # messages.success(request, ("Successfully Login") )
            return redirect('/home')
        else:
            return HttpResponse('Unsuccessfully Login') 
             

    return render(request,'User/login.html')


@login_required(login_url='/login')
def user_logout(request) :
    logout(request)
    # messages.success(request, ("Successfully Logout") )
    return redirect('/home')



# @login_required(login_url='login')
def edit_info(request):
    if request.method == 'POST':
        # Extract data from the request
        email = request.user.username
        charity_name = request.POST.get('charity_name')
        charity_id = request.POST.get('charity_id')
        charity_address = request.POST.get('charity_address')
        charity_city = request.POST.get('charity_city')
        charity_state = request.POST.get('charity_state')
        charity_zipcode = request.POST.get('charity_zipcode')
        

        # Create and save the CustomCharityUser object
        CustomCharityUser.objects.filter(email=email).update(
            charity_name=charity_name,
            charity_id=charity_id,
            charity_address=charity_address,
            charity_city=charity_city,
            charity_state=charity_state,
            charity_zipcode=charity_zipcode
        )
        return HttpResponse('Charity user info edited successfully!') 
    # return render(request,'edit_info.html', {details:'details'})
    
    return render(request,'User\edit_info.html')
    # return HttpResponse('Charity user info edited successfully!') 
    



 
def home(request):
    return render(request,'User/home.html')
    

@login_required(login_url='/login')
def complaint(request):
    if request.method == 'POST':
        # data to write in the database
        # Here er use Ai model for image classification and store it in database
        
        complint_name = request.POST.get('complaint_name')
        crime_type = request.POST.get('crime_type')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        crime_date = request.POST.get('crime_date')
        description = request.POST.get('description')
        

        # Create and save the CustomUser object if necessary
        # (Assuming the user is logged in and their ID is available in request.user.id)
        
        

        # Create and save the Complaint object
        complaint = Complaint(
            complint_name=complint_name,
            user = request.user,
            crime_type=crime_type,
            address=address,
            city=city,
            country=country,
            state=state,
            zipcode=zipcode,
            crime_date=crime_date,
            description=description,
            status="Under checking"
        )
        complaint.save()
        
    return render(request,'User/complaint.html')
    # return HttpResponse('File a Compliant here')



@login_required(login_url='/login')
def ananomuscomplaint(request):
    if request.method == 'POST':
        complaint(request)
    
    # return HttpResponse('File a Ananomus Compliant here') 
    return render(request,'User/complaint.html')

def about_us(request):
    return render(request,'User/about.html')
    # return HttpResponse('here is about page') 

def blogs(request):
    return render(request,'User/blogs.html')


@login_required(login_url='/login')
def write_blog(request):
    if request.method == 'POST': # with Condition decorator
        #whenever a user is logged in then it can edit the blog
        create_blog(request)
    return render(request,'User/write_bolg.html')
        
    
def events(request):

    return render(request,'display_event.html')

# def upcoming_events(request): #it will include in event view
#     return render(request,'upcoming_events.html')


@login_required(login_url='/login')
def events_registrations(request):
    if request.method == 'POST': # with Condition decorator
        # data to write in the database
        # Here er use Ai model for image classification and store it in database
            print('Registration of event ')
     
    return render(request,'events_registration.html')
    
def news(request):
    return render(request,'news.html')
    

def help(request):
    #it provide some of questions and answer 
    # return render(request,'help.html')
    return HttpResponse('help page')



def donation(request): # with Condition decorator
    if request.method == 'POST':
        # data to write in the database
        # Here er use donation logic
        
        # Extract data from the request
        donation_id = request.POST.get('donation_id')
        donor = request.POST.get('donor')
        beneficiary = request.POST.get('beneficiary')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        transaction_method = request.POST.get('transaction_method')

        # Create and save the Donation object
        donation = Donation.objects.create(
            donation_id=donation_id,
            donor=donor,
            beneficiary=beneficiary,
            amount=amount,
            date=date,
            transaction_method=transaction_method
        )
        return HttpResponse('Donation recorded successfully!')
       
    
    return render(request,'donation.html')



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