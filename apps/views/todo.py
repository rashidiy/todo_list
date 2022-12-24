from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from apps.models import Task


class TodoListView(LoginRequiredMixin, ListView):
    template_name = 'apps/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user_id=self.request.user.pk)
