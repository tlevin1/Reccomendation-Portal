from django import forms
from .models import Upload

class Uploadform(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('name', 'type', 'pdf')