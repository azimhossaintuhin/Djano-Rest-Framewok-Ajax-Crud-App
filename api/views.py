from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

@api_view(["GET"])
def api_urls(request):
    api_urls = {
        'List': "/task-list/",
        "Details" : "/task-details/<str:pk>/",
        "Create" : "/task-create/",
        "Update" : "/task-update/<str:pk>/",
        "Delete" : "/task-delete/<str:pk>/",
    }
    return Response(api_urls)


@api_view(["GET"])
def Tasklist(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks , many=True)
    return Response(serializer.data)

@api_view(["GET"])
def Taskdetails(request , pk):
    tasks = Task.objects.get(pk = pk)
    serializer= TaskSerializer(tasks , many = False)
    return Response(serializer.data)

@api_view(["POST"])
def createtask(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()   
    return Response(serializer.data)

@api_view(["POST"])

def UpdateTask(request , pk):
    task = Task.objects.get(pk=pk)
    serializer  = TaskSerializer(instance=task , data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def Deletetask(request , pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return Response("item deleted successfully !")
