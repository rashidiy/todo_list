from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from .views import AuthRegisterView
from .views.auth import AuthLoginView
from .views.todo import TodoListView, TodoReorder, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('accounts/register', AuthRegisterView.as_view(), name='register'),
    path('accounts/login', AuthLoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),

    path('', TodoListView.as_view(), name='todo'),
    path('todo-reorder', TodoReorder.as_view(), name='todo_reorder'),
    path('todo-create', TodoCreateView.as_view(), name='todo_create'),
    path('todo_update/<int:pk>', TodoUpdateView.as_view(), name='todo_update'),
    path('todo_delete/<int:pk>', TodoDeleteView.as_view(), name='todo_delete'),
]
