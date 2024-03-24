"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from catalog import views
from django.urls import path, include
from catalog import models

urlpatterns = [
    
    #path('', views.page.as_view(), name='button_page'),#lets urls.py read home button html code
    path('', views.button_page, name='button_page'),

    #TEST
    #path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    #path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signupquestions', views.signupquestions, name='signupquestions'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),

    path('admin/', admin.site.urls),
    #path("login/", include("django.contrib.auth.urls")), #lets other users in test
    #path('login/', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    

    #path('', views.login, name="login"),
    #path("username/", views.username, name="username"),
    #path("password/", views.password, name="password"),
    path('', views.button_page, name='button_page'),

    path('username/', views.username, name='username'), #returning user button
    path('create/', views.create, name='create'), #create an account button

    #path('table', models.Subject, name='english')

    
]


