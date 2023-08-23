from django import forms
from .models import ToDoModel

class TodoForms(forms.ModelForm):
    task_name_uz = forms.CharField()
    task_name_ru = forms.CharField(required=False)
    task_name_en = forms.CharField(required=False)

    task_description_uz = forms.CharField()
    task_description_ru = forms.CharField(required=False)
    task_description_en = forms.CharField(required=False)

    class Meta:
        model = ToDoModel
        exclude = ['task_name','task_description']
