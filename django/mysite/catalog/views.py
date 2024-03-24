from django.shortcuts import redirect, render
from django.http import HttpResponse 
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
#from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import authenticate, login, logout
from django.db import models
from django import forms


from mysite import settings
#from . tokens import generate_token

# Create your views here.

#class page(TemplateView):
#    template_name = 'button_page.html'

def button_page(request):
    return render(request, 'button_page.html')


#def start(request):
#    return render(request, 'button_page.html')

#class login(TemplateView):
#    template_name = 'login.html'
    

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
       
        
        
        return redirect('signupquestions')
        
    return render(request, "authentication/signup.html")

def signupquestions(request):
    if request.method == "POST":
        grade = request.POST['grade']
        favoritesubject = request.POST['favsubj']
        learning_style = request.POST['learnstyle']
       
        return redirect('signin')
                
    return render(request, "authentication/signupquestions.html")

        
        #    grade = request.POST['What grade are you in?']


        #return redirect('signin')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        #if user is not None:
            #login(request, user)
            #fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            #return render(request, "authentication/index.html",{"fname":fname})
        
        return redirect('home')

    return render(request, "authentication/signin.html")

#Here is the home screen, contains all course work and such. Asks for what subject to work on, accesses shop
def home(request):
    if request.method == 'POST':

        HttpResponse('What would you like to study? Choose from English, Math, Science or History.')

        return redirect('signin')
                
    return render(request, "authentication/signupquestions.html")
    
'''
def home(request):
        #messages.success(request, 'What would you like to study? Choose from English, Math, Science or History.')
    if request.method=='POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            form.save_m2m() # needed since using commit=False
        else:
            form = ProfileForm()

    return render_to_response(template_name, {"profile_form": form}, context_instance=RequestContext(request))
'''
'''
        user = authenticate(pref_subject)

        return redirect('signin')
    
    return render(request, "home.html")

    '''

    



#def subjects(request):
#    if request.method == 'POST':



def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')




#def login(request):
#    return HttpResponse("Are you a returning learner?")

def username(request):
   return HttpResponse("What's your username?")

#def password(request):
#    return HttpResponse("What's your password?")


def create(request):
    return HttpResponse("Welcome! Let's create an account. What would you like your username to be?")


