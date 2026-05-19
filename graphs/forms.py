from django import forms
from .models import GraphUpload

class GraphUploadForm(forms.ModelForm):
    class Meta:
        model = GraphUpload
        fields = ['image']