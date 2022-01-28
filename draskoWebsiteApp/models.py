from email import message
from django.db import models
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


