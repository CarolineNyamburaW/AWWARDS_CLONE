from django.shortcuts import render, redirect
from .models import Photo

from django.contrib import messages
from awwwardzapp.models import *


# Create your views here.

def home(request):
  photos =request.GET.get('photos')


  photos = Photo.objects.all()
  context = {'photos': photos}
  return render(request, 'awwwardzapp/home.html', context)

def viewProject(request, cn):
  photo = Photo.objects.get(id=cn)
  return render(request, 'awwwardzapp/project.html', {'photo':photo})

def addProject(request):


  return render(request, 'awwwardzapp/add.html', )

