from django.views.generic import ListView


class TodoListView(ListView):
    template_name = 'apps/task_list.html'