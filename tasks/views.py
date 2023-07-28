from django.shortcuts import render, redirect

from tasks.forms import CreateTask, DeleteTask
from tasks.models import Task


# Create your views here.
def create_task(request):
    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            task = form.save()
            task.assigned_to = request.user
            task.save()
            return redirect('create task')
    else:
        form = CreateTask()

    context = {
        'form': form,
    }
    return render(request, 'tasks/create.html', context)


def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('all tasks')
    else:
        form = CreateTask(instance=task)

    context = {
        'form': form,
        'task': task,
    }
    return render(request, 'tasks/edit.html', context)


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteTask(request.POST, instance=task)
        if form.is_valid():
            task.delete()
            return redirect('all tasks')
    else:
        form = DeleteTask()

    context = {
        'task': task,
        'form': form,
    }
    return render(request, 'tasks/delete.html', context)


def task_details(request, pk):
    task = Task.objects.get(pk=pk)
    context = {
        'task': task,
    }
    return render(request, 'tasks/details.html', context)


def all_tasks(request):
    all_tasks = Task.objects.all()
    context = {
        'all_tasks': all_tasks,
    }
    return render(request, 'tasks/all_tasks.html', context)
