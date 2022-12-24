from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views.generic import CreateView

from apps.forms import UserRegisterForm


# Create your views here.


class CreateUserView(CreateView):
    form_class = UserRegisterForm
    template_name = 'apps/register.html'

    def form_valid(self, form):
        form.instance.password = make_password(form.instance.password1)
        return super().form_valid(form)

