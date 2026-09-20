from django import forms
from .models import Task
from django.core.exceptions import ValidationError


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'done', 'category']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title or not title.strip():
            raise ValidationError(
                "Task name can't be empty or consists of white spaces only!")

        title = title.strip()
        if len(title) < 3:
            raise ValidationError(
                "Task name should be at least 3 chatacters long!")

        return title
