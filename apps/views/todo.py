from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView

from apps.forms import PositionForm
from apps.models import Task


class TodoListView(LoginRequiredMixin, ListView):
    template_name = 'apps/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TodoReorder(View):
    def post(self, request):
        form = PositionForm(request.POST)

        if form.is_valid():
            position_list = form.cleaned_data["position"].split(',')

            with transaction.atomic():
                self.request.user.set_task_order(position_list)

        return reverse_lazy('todo')


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreateView, self).form_valid(form)
