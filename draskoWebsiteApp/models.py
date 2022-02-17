from email import message
from django.db import models
from django import forms
import re
# import bcrypt

class UserManager(models.Manager):
    def user_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(postData['full_name']) < 2:
            errors ['full_name'] = "Full Name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = "Invalid email address!"
        if len(postData['email']) == 0:
            errors ['email'] = "Email required"
        return errors

# class MyProjectManager(models.Manager):
#     def my_project_validator(self, postData):
#         errors = {}
#         # if

class User(models.Model):
    full_name=models.CharField(max_length=255)
    company=models.CharField(max_length=45)
    email=models.EmailField(max_length=70,blank=True,unique=True)
    phone = models.CharField(max_length=255, null=True)
    message = models.TextField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

class MyProject(models.Model):
    PROJECT_CHOICES = [('0','Not Sure'),('1','Web Design & Development'),('2','Mobile App Design & Development'),('3','Digital Marketing'),('4','Digital Design')]
    project=forms.ChoiceField(choices=PROJECT_CHOICES, widget=forms.RadioSelect)
    TIMELINE_CHOICES = [('0','Not Sure'),('1','1 Month'),('2','6 Months'),('3','1 Year'),('4','1.5 Years'),('5','2+ Years')]
    timeline=forms.ChoiceField(choices=TIMELINE_CHOICES, widget=forms.RadioSelect)
    SIZE_OF_PROJECT_CHOICES = [('0','Not Sure'),('1','Mini'),('2','Small'),('3','Medium'),('4','Large')]
    size_of_project=forms.ChoiceField(choices=SIZE_OF_PROJECT_CHOICES, widget=forms.RadioSelect)
    INDUSTRY_CHOICES = [('0','FinTech'),('1','Hospitality'),('2','Manufacturer'),('3','Retail'),('4','Real Estate'),('5','Logistics'),('6','Healthcare'),('7','Beauty & Wellness'),('8','Education'),('9','Sports'),('10','Travel & Transportation'),('11','Other')]
    industry=forms.ChoiceField(choices=INDUSTRY_CHOICES, widget=forms.RadioSelect)
    services=models.ManyToManyField(User, related_name="projects")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # my_projects=MyProjectManager()




