from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import LOR
from django import http
from . import models
from . import form



# stub for home page
def index(request):
    return HttpResponse('Letters of Recommendation index')


# display table of writer actions
# actions are: accept, deny, review, complete
@login_required
def writer_view(request):
    print(request.method)
    cur_user = request.user
    print(cur_user)
    print("User is ", cur_user)

    # Make sure user is logged in
    # if cur_user.is_authenticated:
    print("User is logged in")
    if request.method == 'POST':
        # Get the list of ids associated with selected table rows
        if not request.POST.getlist('sel_box'):
            # messages.info(request, 'Nothing Selected')
            print('Nothing selected')
        else:
            sel_ids = request.POST.getlist('sel_box')
            # Check which button is pressed
            if 'Accept' in request.POST:
                print('Accept Button pressed')
            elif 'Deny' in request.POST:
                print('Deny Button pressed')
            elif 'Complete' in request.POST:
                print('Complete Button pressed')
            elif 'Review' in request.POST:
                print('Review Button pressed')
    sorted_lors = LOR.objects.filter(writer_email=cur_user.email).order_by("due_date")
    context = {"sorted_lors": sorted_lors}
    return render(request, 'writer_view.html', context)
# else:
    # If no one is logged in, send back to home page
    # return redirect('/')

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
