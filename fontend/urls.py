from django.urls import path
from fontend.views import *

urlpatterns = [
    path("",index,name="home")
]
