from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if 'email_login' in postData:
            if len(postData["email_login"]) < 2:
                errors["email_login"] = "Email cannot be blank!"
            elif not EMAIL_REGEX.match(postData["email_login"]): 
                errors["email_login"] = "Invalid email format!"
        if 'password_login' in postData:
            if len(postData['password_login']) < 8:
                errors["password_login"] = "Please enter a password."
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255, default="user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() 


class Inquiry(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    event = models.CharField(max_length=255)
    event_date = models.DateTimeField()
    order_desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Photo(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    photo_image = models.ImageField(blank=True, null=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)