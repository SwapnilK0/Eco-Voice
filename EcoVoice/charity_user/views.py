from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from .models import CustomCharityUser,Donation,Event,Blog,Profile
from .utils import * 
import uuid

#Login signup and logout is remaining

# Create your views here.


def charity_login(request) :
    if request.method == 'POST':

        email= request.POST.get('email')
        password= request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # messages.success(request, ("Successfully Login") )
            return HttpResponse('Successfully Login')
        else:
            return HttpResponse('Unsuccessfully Login') 
            

    return render(request,'charity_login.html')

def home(request):
    return render(request,'Charity/charity_home.html')
    
    
def display_complaint(request):
    if request.method == 'POST':
        # data to delete from the database
        print('successfuly completed complint or discard ')
    
    # Here Show the all compliant 

    return render(request,'complaint_form.html')



def create_charity_user(request):
    if request.method == 'POST':
        # Extract data from the request
        email = request.POST.get('email')
        
        password = request.POST.get('password')

        # Create and save the CustomCharityUser object
        charity_user = CustomCharityUser.objects.create(email=email,)
        charity_user.set_password(password)
        p_obj = Profile.objects.create(
            user=charity_user,
            email_token = str(uuid.uuid4())
                                       
        )
        send_email_token(email, p_obj.email_token)
       
        return HttpResponse('Verification is send successfully!')
       
            
    else:
        return render(request,'Charity/signup_charity.html')



def verify(request, token):
    # try:
        obj = Profile.objects.filter(email_token=token).first()
        if obj:
            obj.is_verified = True
            obj.save()
            
            return redirect('edit_info.html')
        else :
            return HttpResponse('invalid!')
            
        
    # except Exception as e:
    #     return HttpResponse('The link is invalid or broken!')


def edit_info():
    if request.method == 'POST':
        # Extract data from the request
        charity_name = request.POST.get('charity_name')
        charity_id = request.POST.get('charity_id')
        charity_address = request.POST.get('charity_address')
        charity_city = request.POST.get('charity_city')
        charity_state = request.POST.get('charity_state')
        charity_zipcode = request.POST.get('charity_zipcode')
        password = request.POST.get('password')

        # Create and save the CustomCharityUser object
        charity_user = CustomCharityUser.objects.create(
            password=password,
            email=email,
            charity_name=charity_name,
            charity_id=charity_id,
            charity_address=charity_address,
            charity_city=charity_city,
            charity_state=charity_state,
            charity_zipcode=charity_zipcode
        )
        return HttpResponse('Charity user info edited successfully!') 
    # return render(request,'edit_info.html', {details:'details'})
    # return render(request,'edit_info.html')
    return HttpResponse('Charity user info edited successfully!') 
    



def about(request):
    
    return render(request,'Charity/about.html')
    # return HttpResponse('here is about page')


def blogs(request):
    if request.method == 'POST': 
        create_blog(request)
    
    
    return render(request,'Charity/blogs.html')
    
    
def create_blog(request):
    # Extract data from the request
    author_name = request.POST.get('author_name')
    blog_heading = request.POST.get('blog_heading')
    blog_description = request.POST.get('blog_description')
    uploaded_date = request.POST.get('uploaded_date')

    # Create and save the Blog object
    blog = Blog.objects.create(
        author_name=author_name,
        blog_heading=blog_heading,
        blog_description=blog_description,
        uploaded_date=uploaded_date
    )
    return HttpResponse('Blog created successfully!')


def create_event(request):
    # Extract data from the request
    event_name = request.POST.get('event_name')
    event_id = request.POST.get('event_id')
    event_address = request.POST.get('event_address')
    event_city = request.POST.get('event_city')
    event_state = request.POST.get('event_state')
    event_host = request.POST.get('event_host')
    event_date = request.POST.get('event_date')

    # Create and save the Event object
    event = Event.objects.create(
        event_name=event_name,
        event_id=event_id,
        event_address=event_address,
        event_city=event_city,
        event_state=event_state,
        event_host=event_host,
        event_date=event_date
    )
    return HttpResponse('Event created successfully!')
    

def events(request):
    
    # return HttpResponse('Event page')  
    return render(request,'Charity/display_event.html')




# def upcoming_events(request): #it will include in event view
#     return render(request,'upcoming_events.html')


def news(request):
    if request.method == 'POST': # with Condition decorator
        #whenever a user is logged in then it can edit the blog
        print('blog editing')
        
    return render(request,'Charity/news.html')
    

def help(request):
    #it provide some of questions and answer 
    # return render(request,'help.html')
    return HttpResponse('help page')


def donation_details(request):
    if request.method == 'GET':
        # Get the logged-in user's charity name
        if request.user.is_authenticated:
            charity_user = CustomCharityUser.objects.get(email=request.user.email)
            charity_name = charity_user.charity_name
        else:
            return HttpResponse('User not logged in')

        # Filter donations where charity name and beneficiary name are the same
        donations = Donation.objects.filter(beneficiary=charity_name)

        # Pass the filtered data to the HTML template
        return render(request, 'donation_details.html', {'donations': donations})
    else:
        return HttpResponse('Invalid request method')






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