from django import forms
from .models import moreinfo

class Infoform(forms.ModelForm):
    class Meta:
        model = moreinfo
        fields = ('name', 'send_to','date','email', 'type', 'description')
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'send_to': forms.TextInput(attrs={'class': 'form-control'}),
                  'date': forms.TextInput(attrs={'class': 'form-control'}),
                  'email': forms.TextInput(attrs={'class': 'form-control'}),
                  'type': forms.TextInput(attrs={'class': 'form-control'}),
                  'description': forms.Textarea(attrs={'class': 'form-control'}),

                  }
        #uses model Upload