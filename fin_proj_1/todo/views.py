from django.http.response import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from django.db.models import Q
import datetime
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

@permission_required('todo.view_task')
def index(request):

    tasks = (Task.objects.filter(user = request.user)).order_by('-created')
    context= {'title':'TODO list', 'tasks':tasks}
    return  render(request,'todo/index.html', context)

@permission_required('todo.add_task')
def create(request):
    
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            added_task = form.save()
            added_task.user  = request.user
            added_task.save()
            messages.success(request, f"Task {added_task.title} was created!")
            return redirect('home')
    form = TaskForm()
    context= {'title': 'Add task', 'form': form, 'now':datetime.datetime.today().strftime("%Y-%m-%d")} 
    return  render(request,'todo/create.html', context)

@permission_required('todo.delete_task')
def delete_todo(request,id):

    if request.method =='POST':
        try:
            del_task =  Task.objects.get(id=id)
            del_task_title = del_task.title
            del_task.delete()
        except:
            return Http404  ('<h1>Something went wrong...TASK NOT FOUND</h1>')  #!!!!!!!!!!!!
        messages.info(request, f'Task "{del_task_title}" has been deleted successfully!')
    return redirect('home')

@permission_required('todo.view_task')
def search(request):
    
    if request.method =='POST':
        searched = request.POST['searched']
        tasks = (Task.objects.filter(user = request.user)).filter(Q(title__icontains=searched) | Q(description__icontains=searched)).order_by('-created')
        context = {'title':'Search result', 'tasks':tasks}
        return  render(request,'todo/index.html', context)
    else:
        context = {'title':'Search result',}
        return  render(request,'todo/index.html', context)

@permission_required('todo.change_task')
def complete_todo(request, id):

    if request.method =='POST':
        task = Task.objects.get(id=id)
        task.complete = not(task.complete)
        task.save()
        if task.complete:
            messages.info(request, f'Task "{task.title}" was completed!')
        else:
            messages.info(request, f'Status of task "{task.title}" was changed.')
    return redirect('home')

@permission_required('todo.change_task')
def edit(request, id):
    
    task = Task.objects.get(id=id)
    current_deadline = task.deadline
    if current_deadline:
        current_deadline = current_deadline.strftime("%Y-%m-%d")
    context = {'title':task.title, 'task':task, 'current_deadline': current_deadline, 'now':datetime.datetime.today().strftime("%Y-%m-%d")}
    return render(request,'todo/edit.html', context)

@permission_required('todo.change_task')
def update(request, id):
    
    if request.method =='POST':
        task = Task.objects.get(id=id)
        task.title = request.POST['title']
        task.description = request.POST['description']
        if request.POST['deadline'] !="":
            task.deadline=request.POST['deadline']
        elif request.POST['deadline'] =="":
            task.deadline=None
        task.created = datetime.datetime.now()
        task.save()
        messages.success(request, f"Task '{task.title}' was updated")
    return redirect('home')

@permission_required('todo.view_task')
def deadline_today(request):
    
    tasks = Task.objects.filter(user = request.user)
    tasks = tasks.filter(deadline=datetime.datetime.now())
    deadline_today = True
    context = {'title':'Deadline today', 'tasks':tasks, 'deadline_today': deadline_today}
    return render(request,'todo/index.html', context)

def register(request):
    
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
           new_user=form.save()
           permission1=Permission.objects.get(name='Can view task')
           permission2=Permission.objects.get(name='Can change task')
           permission3=Permission.objects.get(name='Can delete task')
           permission4=Permission.objects.get(name='Can add task')
           new_user.user_permissions.add(permission1,permission2,permission3,permission4)
           messages.success(request, f"Account was created for {form.cleaned_data['username']}")
           return redirect('login')
        # else:
        #     messages.error(request, f"Account wasn't created!") 
    context = {'form':form}
    return render(request, 'registration/register.html', context)