from django.conf.global_settings import AUTH_PASSWORD_VALIDATORS
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, EmailField, PasswordInput


class UserRegisterForm(ModelForm):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    username = UsernameField()
    email = EmailField()
    password = CharField(min_length=8, validators=AUTH_PASSWORD_VALIDATORS, widget=PasswordInput)
    confirm_password = CharField(min_length=8, widget=PasswordInput)

    def clean_password2(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('confirm_password'):
            raise ValidationError('Ikkala maydon bir biriga mos kelishi shart')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
