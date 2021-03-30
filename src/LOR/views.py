from django.shortcuts import render
from django import http
from . import models
from . import form

# Create your views here.
'''
def view_enter_request(request):
    obj = models.Request_Form.objects.get(id=1)
    request_form = {
        "object" : obj
    }
    return render(request,"LOR/enter_request.html", request_form);
'''


def view_enter_request(request):
    obj = form.RequestForm(request.POST or None)
    if obj.is_valid():
        obj.save()
        return http.HttpResponseRedirect('/')

    request_form = {
        "object": obj
    }
    return render(request,"LOR/enter_request.html", request_form);
