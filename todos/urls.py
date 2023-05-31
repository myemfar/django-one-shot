from django.urls import path
from todos.views import (
    todo_list,
    todo_list_detail,
    create_todo_list,
    todo_list_update,
    todo_list_delete,
    todo_item_create,
)

urlpatterns = [
    path("", todo_list, name="todo_list"),
    path("<int:id>/", todo_list_detail, name="todo_list_detail"),
    path("create/", create_todo_list, name="create_todo_list"),
    path("<int:id>/edit/", todo_list_update, name="todo_list_update"),
    path("<int:id>/delete/", todo_list_delete, name="todo_list_delete"),
    path("items/create/", todo_item_create, name="todo_item_create"),
]
