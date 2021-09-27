from django.urls import path
from . import views

urlpatterns =[
  path('', views.home, name='home'),
  path('project/<str:cn>/', views.viewProject, name='project'),
  path('add/', views.addProject, name='add'),
]