from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import *


# Create your views here.
@login_required
def logoff(request):
    logout(request)
    return redirect('../../')
