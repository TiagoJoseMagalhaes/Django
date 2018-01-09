from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

# Create your views here.
def list(request):
    All_users = User.objects.all()
    template = loader.get_template("list.html")
    context = {"All_users": All_users}
    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template("add.html")
    context = {}
    return HttpResponse(template.render(context,request))

def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context,request))
