from django import forms
from django.db import models
from .models import RequestModel, Upload


# Create your form here.

class RequestForm(forms.ModelForm):
    class Meta:
        model = RequestModel
        fields = [
            'requester',
            'requester_email',
            'position',
            'due_date',
            'writer_name',
            'writer_email',
            'company_name',
            'company_website',
            'company_email',
            'company_recipients',
            'cv',
            'resume',
            'transcript',
            'additional_info',
        ]
        labels = {
            'cv': 'Please put your cv URL into this box',
            'resume': 'Please put your resume URL into this box',
            'transcript': 'Please put your transcript URL into this box',
        }

class Uploadform(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('name', 'type', 'pdf')