
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .import forms, models


class Register(CreateView):
    form_class = forms.RegisterForm
    template_name = "registration.html"
    success_url = "/clients/"


class Login(LoginView):
    form_class = forms.LoginForm
    template_name = "logo.html"
    success_url = "/clients/"


class ClientList(ListView):
    template_name = "clients.html"
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset
