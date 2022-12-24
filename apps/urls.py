from django.urls import path

from .views import CreateUserView

urlpatterns = [
    path('accounts/register', CreateUserView.as_view(), name='register'),
]
