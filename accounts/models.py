from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your models here.
class UserCreate(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()