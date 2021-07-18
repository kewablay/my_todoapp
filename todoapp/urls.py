from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.todo_index, name='todo_index'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo')

]

