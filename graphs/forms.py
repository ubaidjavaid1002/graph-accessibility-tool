from django import forms
from .models import Graph

class GraphUploadForm(forms.ModelForm):
    class Meta:
        model = Graph
        fields = ['image']