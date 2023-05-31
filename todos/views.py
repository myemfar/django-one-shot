from django.shortcuts import render, get_object_or_404
from todos.models import TodoList, TodoItem


# Create your views here.
def todo_list(request):
    todos = TodoList.objects.all()
    context = {
        "todo_list": todos,
    }
    return render(request, "todos/view.html", context)


def todo_list_detail(request, id):
    details = get_object_or_404(TodoList, id=id)
    context = {
        "todo_list_detail": details,
    }
    return render(request, "todos/detail.html", context)
