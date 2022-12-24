from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from apps.forms import PositionForm
from apps.models import Task


class TodoListView(LoginRequiredMixin, ListView):
    template_name = 'apps/task_list.html'
    model = Task

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            'tasks': self.request.user.task_set.all(),
            'count': self.request.user.task_set.filter(status=False).count()
        }
        return context

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
    fields = ('title', 'description', 'status')
    success_url = reverse_lazy('todo')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreateView, self).form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ('title', 'description', 'status')
    success_url = reverse_lazy('todo')


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('todo')

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(user=user)


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'todo'
    template_name = 'apps/task.html'
