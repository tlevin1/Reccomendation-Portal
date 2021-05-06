from django import forms
from django.db import models
from .models import RequestModel
from Authentication.models import LorUser as User
from Authentication.models import UserRoles as Roles

# Create your form here.

class RequestForm(forms.ModelForm):
    class Meta:
        model = RequestModel
        fields = [
            'requester_fk',
            'position',
            'due_date',
            'writer_fk',
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

