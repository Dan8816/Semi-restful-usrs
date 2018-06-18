from django.shortcuts import render, HttpResponse, redirect
from apps.first_app.models import User
from django.contrib import messages
from time import localtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.
# the index function is called when root is visited
def index(request):
    context = {
        "users": User.objects.all()        
    }
    return render(request, "first_app/index.html", context)

def new(request):
    return render(request, "first_app/new.html")

def show(request, id):
    context = {
        "users" : User.objects.get(id=id)
    }
    return render(request, "first_app/userid.html", context)

def edit(request, id):
    context = {
        "users" : User.objects.get(id=id)
    }
    return render(request, "first_app/edit.html", context)

def create(request):
    User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"])
    return redirect('/users')

def destroy(request, id):
    d = User.objects.get(id=id)
    d.delete()
    return redirect('/users')

def update(request, id):
    s = User.objects.get(id=id)
    s.first_name=request.POST["first_name"]
    s.last_name=request.POST["last_name"]
    s.email=request.POST["email"]
    s.save()
    return redirect('/users')