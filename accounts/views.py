from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import UserCreate

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreate
    success_url = reverse_lazy('login')
    template_name = 'signup.html'