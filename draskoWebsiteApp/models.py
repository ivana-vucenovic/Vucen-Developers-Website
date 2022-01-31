from email import message
from django.db import models
from django import forms
import re
# import bcrypt

class UserManager(models.Manager):
    def user_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(postData['first_name']) < 2:
            errors ['first_name'] = "First Name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = "Invalid email address!"
        if len(postData['email']) == 0:
            errors ['email'] = "Email required"
        return errors

class MyProjectManager(models.Manager):
    def my_project_validator(self, postData):
        errors = {}
        # if

class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    company_name=models.CharField(max_length=45)
    email=models.EmailField(max_length=70,blank=True,unique=True)
    phone_number = models.CharField(max_length=255, null=True)
    message = models.TextField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

class MyProject(models.Model):
    PROJECT_CHOICES = [('0','Not sure'),('1','Web Design & Development'),('2','Mobile App Design & DEvelopment'),('3','Digital Marketing'),('4','Digital Design')]
    project=forms.ChoiceField(choices=PROJECT_CHOICES, widget=forms.RadioSelect)
    timeline=
    size_of_project=
    INDUSTRY_CHOICES = [('0','FinTech'),('1','Hospitality'),('2','Manufactuer'),('3','Retail'),('4','Real Estate'),('5','Logistics'),('6','Healthcare'),('7','Beauty & Wellness'),('8','Education'),('9','Sports'),('10','Travel & Transportation'),('11','Other')]
    industry=forms.ChoiceField(choices=INDUSTRY_CHOICES, widget=forms.RadioSelect)
    services=models.ManyToManyField(User, related_name="projects")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    my_projects=MyProjectManager()




