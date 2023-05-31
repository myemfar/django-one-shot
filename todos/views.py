from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoForm, TodoItemForm


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


def todo_list_delete(request, id):
    model_instance = TodoList.objects.get(id=id)
    if request.method == "POST":
        model_instance.delete()
        return redirect("todo_list")
    return render(request, "todos/delete.html")


def todo_item_create(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect("todo_list_detail", id=form.list.id)
    else:
        form = TodoItemForm()
    context = {
        "form": form,
    }
    return render(request, "todos/itemcreate.html", context)


def todo_item_update(request, id):
    post = get_object_or_404(TodoItem, id=id)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=post)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect("todo_list_detail", id=form.list.id)
    else:
        form = TodoItemForm(instance=post)
    context = {
        "form": form,
        "object": post,
    }
    return render(request, "todos/edititem.html", context)
