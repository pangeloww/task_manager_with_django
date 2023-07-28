from django import forms

from tasks.models import Task


class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'choices']
        labels = {
            'choices': 'Status'
        }


class DeleteTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = []

