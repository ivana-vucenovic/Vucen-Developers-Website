from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .models import MyProject

# import bcrypt

def index(request):
    return render(request, 'index.html')

def contact(request):
    users = User.objects.all()
    context ={
        'users': users
    }
    return render(request, 'contact.html', context)

def create(request):
    User.objects.create(full_name = request.POST("Name"), company = request.POST("Company"), email = request.POST("Email"), phone = request.POST("Phone"), message = request.POST("Message"))
    return redirect()

def about(request):
    pass

def services(request):
    pass

def privacy(request):
    return render(request, 'privacyPolicy.html')

