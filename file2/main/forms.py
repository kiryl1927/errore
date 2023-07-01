from dataclasses import fields
from .models import Task
from django.forms import ModelForm, widgets, TextInput

class TaskForm(ModelForm):
    class Meta:
        models = Task
        fields = ("title", "task")
        widgets = {'title': TextInput(attrs={'class':'form-control', 'placeholder':'введите название'}),
                   'task': TextInput(attrs={'class': 'form-control', 'placeholder': 'введите описание'}),
                   }