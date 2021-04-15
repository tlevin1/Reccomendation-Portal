from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import LOR, Req_a,UpdateRequest
from datetime import datetime
from django import http
from . import models
from . import form
from django.http import HttpResponseRedirect
from django.urls import reverse





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

def view_enter_request(request):
    obj = form.RequestForm(request.POST or None)
    if obj.is_valid():
        obj.save()
        return http.HttpResponseRedirect('/')

    request_form = {
        "object": obj
    }
    return render(request,"LOR/enter_request.html", request_form);

def writer_req(request):
    #form = ReqForm()

    answer = Req_a.objects.all()
    if request.method == 'POST':
            req = Req_a.objects.get(name=request.POST.get('name'))
            if(request.POST.get('status')):
                #if there is post resquest, copy information
                req.answer = request.POST.get('status')
                req.A_date = datetime.now()
                req.save()
        #save into database

    return render(request, 'LOR/requests.html', {'answers': answer})

def writer_review(request):
    #all data
    obj = models.LOR.objects.all()
    request_form = {
        "object": obj
    }
    print(obj)
    if 'Cover Letter' in request.POST:
        print('Cover Letter Button pressed')
    elif 'Resume' in request.POST:
        print('Resume Button pressed')
    elif 'Transcript' in request.POST:
        print('Transcript Button pressed')
    elif 'Additional Information' in request.POST:
        print('Review Button pressed')
    elif 'Next' in request.POST:
        print('Next Button pressed')
    return render(request, 'LOR/writer_review.html', {'objs': obj})


#request review
@login_required
def requester_review(request):
    # all data - model
    obj = LOR.objects.all()
    print(obj)
    print(request.method)
    cur_user = request.user
    print(cur_user)
    print("User is ", cur_user)

    # Make sure user is logged in
    # if cur_user.is_authenticated:
    print("User is logged in")
    # Check which button is pressed
    #POST - result of form submission
    if request.method == 'POST':
        if not request.POST.getlist('sel_box'):
            #messages.info(request, 'Nothing Selected')
            print('Nothing selected')
        if 'New Request' in request.POST:
            print("Request Button Selected")
        elif 'Review/Update' in request.POST:
            print('Review/Update pressed')
            #return render(request, 'LOR/request_page.html', {'objs': obj})
            return HttpResponseRedirect('req_page')
        elif 'Withdraw' in request.POST:
            print('Withdraw Button pressed')
        else:
            sel_ids = request.POST.getlist('sel_box')


    return render(request, 'LOR/requester_review.html', {'objs': obj})


#added for review/update request
def requester_view_particular_request(request):
    results = models.UpdateRequest.objects.all()
    print(results)
    print(request.method)
    #returning dictionary
    return render(request,'LOR/request_page.html',{"res ": results})