from django.urls import path

from .views import category_list

app_name = "categories"

urlpatterns = [
    path("all/" , category_list , name = "categories")
]