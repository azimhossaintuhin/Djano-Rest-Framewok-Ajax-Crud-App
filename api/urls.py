from django.urls import path
from api.views import *
urlpatterns = [
    path("",api_urls, name="tasklist"),
    path("task-list/", Tasklist, name="tasklist"),
    path("task-details/<str:pk>/", Taskdetails , name = "taskdetalis"),
    path("task-create/" , createtask, name="Task-create"),
    path("task-update/<str:pk>/", UpdateTask , name = "taskupdate"),
    path('task-delete/<str:pk>/',Deletetask , name = "taskdelete")

]
