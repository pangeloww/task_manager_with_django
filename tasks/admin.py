from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    raw_id_fields = ('assigned_to',)


admin.site.register(Task, TaskAdmin)
