from django.forms import ModelForm
from django import forms
from models import *
 class signupform(ModelForm):
     class meta:
         model=signup
         fields=['email','password']
         widgets={
             'password':forms.PasswordInput()
         }