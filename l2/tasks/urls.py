from django.urls import path

from .views import task_list

app_name = "tasks"

urlpatterns = [
    path("" , task_list , name = "tasks_list")
]