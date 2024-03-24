from django.urls import path
from . import views 

urlPatterns = [
    path("/demo", views.demo, name="demo")
]