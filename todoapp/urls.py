from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home_page"),
    path('add-todo', add_todo, name="add_todo"),
    path('update/<int:todo_id>', update_todo, name='update_todo'),
    path('delete/<int:todo_id>', delete_todo, name='delete_todo'),
]