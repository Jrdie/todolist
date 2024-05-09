from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def home(request):
    data = Todo.objects.all()

    return render(request, "home.html", {'data': data})


def add_todo(request):
    if request.method =='POST':

        title = request.POST.get("title")
        description = request.POST.get("description")

        elem = Todo()
        elem.title = title
        elem.description = description

        elem.save()

        return redirect('home_page')
    
    return render(request, "add_todo.html")


def update_todo(request, todo_id):
    upd_data = Todo.objects.get(id = todo_id)

    if request.method =='POST':

        title = request.POST.get("title")
        description = request.POST.get("description")
        status = request.POST.get("status")

        elem = Todo.objects.get(id = todo_id)
        elem.title = title
        elem.description = description

        if status is None: 
            elem.status = False
        else:
            elem.status = True

        elem.save()

        return redirect('home_page')

    return render(request, "update_todo.html", {'upd_data': upd_data})


def delete_todo(request, todo_id):
    del_todo = Todo.objects.get(id = todo_id)
    del_todo.delete()

    return redirect('home_page')