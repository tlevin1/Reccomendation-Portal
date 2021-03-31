from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
'''
@staff_member_required
def index(request):
    if (LorUser.objects.filter(base_user=request.user).first() is None):
        LorUser.objects.create(base_user=request.user, first_name=request.user.username, role=UserRoles.ADMIN)
    return HttpResponse('auth screen')
'''

'''
@login_required
def index(request):
    if (LorUser.objects.filter(base_user=request.user).first() is None):
        LorUser.objects.create(base_user=request.user, first_name=request.user.username, role=request.user.group)
    return HttpResponse('auth screen')
'''

@login_required
def index(request):
    return HttpResponse('You are Authenticated')