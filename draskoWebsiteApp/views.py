from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# import bcrypt

def index(request):
    return render(request, 'index.html')

def contact(request):
    users = User.objects.all()
    context ={
        'users': users
    }
    return render(request, 'contact.html', context)
