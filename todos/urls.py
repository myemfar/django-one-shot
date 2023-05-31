from django.urls import path
from todos.views import (
    todo_list,
    todo_list_detail,
    create_todo_list,
    todo_list_update,
)

urlpatterns = [
    path("", todo_list, name="todo_list"),
    path("<int:id>/", todo_list_detail, name="todo_list_detail"),
    path("create/", create_todo_list, name="create_todo_list"),
    path("<int:id>/edit", todo_list_update, name="todo_list_update"),
]
