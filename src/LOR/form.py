from django import forms
from django.db import models
from .models import RequestModel


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

