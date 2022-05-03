from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

#!tasksView
@api_view(['GET', 'POST'])
@csrf_exempt
def tasksView(request):
    if(request.method == 'GET'):
        print('Isledi')
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        print(request.data)
        print('POST request atildi')
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('Save Oldu Databaseye POST requestden gelen deyer')
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@csrf_exempt
def taskDetailUpdate(request,pk):
    try:
        task = Task.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    if(request.method == 'PUT'):
        #PUT == UPDATE method
        print('Update Olmadan Once ', request.data)
        serializer = TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('Update Oldu')
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif(request.method == 'DELETE'):
        task.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    