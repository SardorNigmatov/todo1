from django.contrib import admin
from .models import ToDoModel
from .forms import TodoForms

# Register your models here.

class ToDoAdmin(admin.ModelAdmin):
    form = TodoForms
    list_display = ['task_name','done']
    search_fields = ['task_name','done']

admin.site.register(ToDoModel,ToDoAdmin)