from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField(max_length=20,null=True,blank=True)
    subject=models.CharField(max_length=20,null=True,blank=True)
    message=models.TextField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.name