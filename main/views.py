from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm, TodoForm
from .models import Todo

# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def features(request):
    return render(request, 'main/features.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # In a real app, you'd handle the form data (e.g., send an email)
            return redirect('home') 
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def todo(request):
    todos = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    return render(request, 'main/todo.html', {'todos': todos, 'form': form})

def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'main/todo_edit.html', {'form': form})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo')

def todo_mark_done(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo')
