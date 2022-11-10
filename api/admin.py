from django.contrib import admin
from api.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ("task", "completed", )

admin.site.register(Task, TaskAdmin)