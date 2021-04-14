from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime
from django import http
from . import models
from LOR.models import RequestModel

# Create your views here.
def request_view(request):
    forms = RequestModel.objects.all()
    obj = {
        'obj':forms
    }
    return render(request,"requestor_manage/request_view.html", obj);

