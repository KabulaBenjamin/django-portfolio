# projects/forms.py

from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title', 'description', 'category', 'technologies',
            'github_link', 'live_demo', 'date_completed'
        ]
        widgets = {
            'date_completed': forms.DateInput(attrs={'type': 'date'})
        }