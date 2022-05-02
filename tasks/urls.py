from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/',tasksView,name='tasksView'),
    path('tasks/<int:pk>/',taskDetailUpdate,name='taskDetailUpdate')
]
