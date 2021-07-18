from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
from django.utils import timezone


def home(request):
    return render(request, 'todoapp/home.html')


def todo_index(request):
    todo_item_list = TodoItem.objects.order_by('-date_added')
    context = {
        'todo_item_list': todo_item_list,
    }
    return render(request, 'todoapp/todo_index.html', context)


def add_todo(request):
    add_todo = request.POST["add_todo"]
    time = timezone.now()
    TodoItem.objects.create(todo=add_todo, date_added=time)
    return HttpResponseRedirect("/todoapp/")


def delete_todo(request, todo_id):
    TodoItem.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/todoapp/")


