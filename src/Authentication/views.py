from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import LorUser, UserRoles
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


# Create your views here.
@staff_member_required
def index(request):
    if (LorUser.objects.filter(base_user=request.user) is None):
        LorUser.objects.Create(request.user, first_name=request.user.username, role=UserRoles.ADMIN)
    return HttpResponse('auth screen')
