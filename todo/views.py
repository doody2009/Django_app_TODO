from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from todo.models import Todo

def general(request):
    taches = Todo.objects.all()
    return render(request,'todo.html', {'taches': taches})

def addTodo(request):
    new_elt = Todo(name = request.POST['content'])
    new_elt.save()
    return HttpResponseRedirect('/general/')


def deleteTodo(request, todo_id):
    elt_todelete = Todo.objects.get(id = todo_id)
    elt_todelete.delete()
    return HttpResponseRedirect('/general/')

##mettez des commentaires explicatifs
