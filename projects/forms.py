from django import forms

from projects.models import Project, File


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project


class FileForm(forms.ModelForm):
    class Meta:
        model = File
