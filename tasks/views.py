from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
import json
from django.http import HttpResponse

def index(request):
    tasks = Task.objects.all().order_by('priority')
    if request.method == 'POST':
        title = request.POST['title']
        priority = request.POST.get('priority', 1)
        new_task = Task(title=title,priority=priority)
        new_task.save()
        return redirect('index')

    return render(request, 'tasks/index.html', {'tasks': tasks})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
         task.title = request.POST['title']
         task.priority = request.POST.get('priority', task.priority)
         task.save()
         return redirect('index')
    return render(request, 'tasks/edit.html', {'task':task})
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')

def export_tasks(request):
    tasks = list(Task.objects.all().values())
    response = HttpResponse(json.dumps(tasks), content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename=tasks.json'
    return response

def import_tasks(request):
    if request.method == 'POST':
        file = request.FILES['file']
        tasks_data = json.load(file)
        for task_data in tasks_data:
            Task.objects.update_or_create(id=task_data['id'], defaults=task_data)
        return redirect('index')
    return render(request, 'tasks/import.html')

