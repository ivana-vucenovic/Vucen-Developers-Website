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

def about(request):
    pass

def privacy(request):
    return render(request, 'privacyPolicy.html')