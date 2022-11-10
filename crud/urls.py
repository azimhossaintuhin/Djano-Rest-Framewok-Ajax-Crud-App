
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,include('fontend.urls'),name='fontend'),
    path("api/", include("api.urls") , name="api")
]
