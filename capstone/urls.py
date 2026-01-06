from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("task/create", views.create_task, name="create_task"),
    path("task/<int:task_id>/toggle", views.toggle_task, name="toggle_task"),
    path("task/<int:task_id>/delete", views.delete_task, name="delete_task")
]
