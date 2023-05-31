from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoForm


# Create your views here.
def todo_list(request):
    todos = TodoList.objects.all()
    context = {
        "todo_list": todos,
    }
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    details = get_object_or_404(TodoList, id=id)
    context = {
        "todo_list_detail": details,
    }
    return render(request, "todos/detail.html", context)


def create_todo_list(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TodoForm()
    context = {
        "form": form,
    }
    return render(request, "todos/create.html", context)


def todo_list_update(request, id):
    post = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = TodoForm(instance=post)
    context = {
        "form": form,
        "object": post,
    }
    return render(request, "todos/edit.html", context)
