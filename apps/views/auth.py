from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.forms import UserRegisterForm


# Create your views here.


class AuthRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'apps/register.html'
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        form.instance.password = make_password(form.cleaned_data.get('password'))
        return super().form_valid(form)


class AuthLoginView(LoginView):
    template_name = 'apps/login.html'
    next_page = reverse_lazy('login')
    form_class = AuthenticationForm
