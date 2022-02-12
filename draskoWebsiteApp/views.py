from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
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

def contactUs(request):
    if request.method == 'POST':
        full_name = request.POST['full_name'],
        company = request.POST['company'],
        email = request.POST['email'],
        phone = request.POST['phone'],
        message = request.POST['message'],

        # send an email
        send_mail(
            'message from' + full_name, 
            company,
            email, # from email
            phone,
            message,
            ['vucendevelopers1@gmail.com'], # To email

        )

        return render(request, 'contact.html', {'full_name': full_name})
    else:
        return render(request, 'contact.html', {})


def create(request):
    User.objects.create(full_name = request.POST("Name"), company = request.POST("Company"), email = request.POST("Email"), phone = request.POST("Phone"), message = request.POST("Message"))
    return redirect()

# def about(request):
#     pass

# def services(request):
#     pass

def privacy(request):
    return render(request, 'privacyPolicy.html')

