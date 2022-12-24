from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from .views import AuthRegisterView
from .views.auth import AuthLoginView
from .views.todo import TodoListView

urlpatterns = [
    path('accounts/register', AuthRegisterView.as_view(), name='register'),
    path('accounts/login', AuthLoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),

    path('todo', TodoListView.as_view(), name='todo'),
]
