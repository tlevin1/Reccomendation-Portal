from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .models import LOR, Req_a, RequestModel
from datetime import datetime
from django import http
from . import models
from . import form
from django.http import HttpResponseRedirect
from django.urls import reverse
from Authentication.models import LorUser as User
from Authentication.models import UserRoles as Roles

# display home page
def index(request):
   cur_user = request.user
   # determine number of requests user made and number of user's actions to write a recommendation
   if cur_user.is_authenticated:
       #numRequests = RequestModel.objects.filter(requester_fk=cur_user).count()
       numRequests = LOR.objects.filter(requester_email=cur_user.email).count()
       numActions = LOR.objects.filter(writer_email=cur_user.email).count()
       print(numRequests, numActions)
   else:
       numRequests = -1
       numActions = -1
   context = {
       "numRequests": numRequests,
       "numActions": numActions,
   }
   return render(request, 'index.html', context)


# Change request status to given new status if current status isn't in invalid_sel list
def change_status(sel_ids, invalid_sel, new_status):
    error = False
    for id in sel_ids:
        lor = LOR.objects.get(id=id)
        if lor.status != new_status:
            if lor.status in invalid_sel:
                error = True
            else:
                lor.status = new_status
                lor.save()
    return error


# display writer dashboard
# actions are: accept, deny, review, complete
@login_required
def writer_view(request):
   print(request.method)
   cur_user = request.user
   print("Logged in user is ", cur_user)

   if request.method == 'POST':
       # Get the list of ids associated with selected table rows
       if not request.POST.getlist('sel_box'):
           # added for home
           if 'Home' in request.POST:
               print('clicked home')
               return redirect(index)
           messages.info(request, 'Nothing Selected')
           # print('Nothing selected')
       else:
           sel_ids = request.POST.getlist('sel_box')
           # Check which button is pressed
           if 'Accept' in request.POST:
               # print('Accept Button pressed')
               new_status = 'Accepted'
               invalid_sel = {'Completed', 'Withdrawn'}
               errmsg = 'Unable to accept a completed or withdrawn request'
               if change_status(sel_ids, invalid_sel, new_status):
                   messages.info(request, errmsg)
           elif 'Deny' in request.POST:
               # print('Deny Button pressed')
               new_status = 'Denied'
               invalid_sel = {'Completed', 'Withdrawn'}
               errmsg = 'Unable to deny a withdrawn or completed request'
               if change_status(sel_ids, invalid_sel, new_status):
                   messages.info(request, errmsg)
           elif 'Complete' in request.POST:
               # print('Complete Button pressed')
               new_status = 'Completed'
               invalid_sel = {'Withdrawn', 'Denied'}
               errmsg = 'Unable to complete a withdrawn or denied request'
               if change_status(sel_ids, invalid_sel, new_status):
                   messages.info(request, errmsg)
           elif 'Review' in request.POST:
               # print('Review Button pressed')
               # display full information of selected requests
               obj = LOR.objects.filter(id__in=sel_ids)
               return render(request, 'LOR/writer_review.html', {'objs': obj})

   # for POST or GET, get logged in writer's requests sorted by due date
   sorted_lors = LOR.objects.filter(writer_email=cur_user.email).order_by("due_date")
   context = {"sorted_lors": sorted_lors}
   return render(request, 'writer_view.html', context)


# display requester dashboard
# actions are: New Request, Review, Withdraw
@login_required
def requester_view(request):
   print(request.method)
   cur_user = request.user
   print("Logged in user is ", cur_user)

   if request.method == 'POST':
       if 'New Request' in request.POST:
           # print('New Request Button pressed')
           return redirect(view_enter_request)

       if not request.POST.getlist('sel_box'):
           # added for home
           if 'Home' in request.POST:
               print('clicked home')
               return redirect(index)
           messages.info(request, 'Nothing selected')
           # print('Nothing selected')
       else:
           # Get the list of ids associated with selected table rows
           sel_ids = request.POST.getlist('sel_box')
           # Check which button is pressed
           if 'Review' in request.POST:
               # print('Review Button pressed')
               if len(sel_ids) > 1:
                   messages.info(request, 'Please only select one request to review/update')
               else:
                   # display the form with data from the selected request
                   lor = LOR.objects.get(id=sel_ids[0])
                   context = {
                       'lor': lor
                   }
                   return render(request, 'updateLOR.html', context)
           elif 'Withdraw' in request.POST:
               # change status to withdrawn if status is not already completed
               # print('Withdraw Button pressed')
               new_status = 'Withdrawn'
               invalid_sel = {'Completed'}
               errmsg = 'Unable to withdraw a completed request'
               if change_status(sel_ids, invalid_sel, new_status):
                   messages.info(request, errmsg)

   # for POST or GET, get logged in user's requests sorted by due date
   sorted_lors = LOR.objects.filter(requester_email=cur_user.email).order_by("due_date")
   context = {"sorted_lors": sorted_lors}
   return render(request, 'requester_view.html', context)


# review or update a recommendation request
@login_required
def updateLOR_view(request):
    if request.method == "POST":
        if 'close_request' in request.POST:
            # no saving form is Close button was pressed
            return redirect(requester_view)
        else:
            # the Save button was pressed
            id = request.POST.get('id')
            lor = LOR.objects.get(id=id)

            # put fields into LOR and save LOR
            lor.due_date = request.POST.get('due_date')
            lor.position = request.POST.get('position')
            lor.company_name = request.POST.get('company_name')
            lor.company_email = request.POST.get('company_email')
            lor.company_website = request.POST.get('company_website')
            lor.company_recipients = request.POST.get('company_recipients')
            lor.resume = request.POST.get('resume')
            lor.cv = request.POST.get('cv')
            lor.transcript = request.POST.get('transcript')
            lor.additional_info = request.POST.get('additional_info')
            lor.save()
            return redirect(requester_view)


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
    obj.fields['requester_fk'].queryset = User.objects.filter(role=Roles.REQUESTER)
    obj.fields['writer_fk'].queryset = User.objects.filter(role=Roles.WRITER)
    if obj.is_valid():
        obj.save()
        # return http.HttpResponseRedirect('/')
        return redirect(requester_view)

    request_form = {
        "object": obj
    }
    return render(request,"LOR/enter_request.html", request_form)


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
   print("inside")
   if request.method == 'POST':
       # close button clicked or no ids passed in, so return to writer dashboard
       return redirect(writer_view)
'''
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
'''

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
    obj = models.UpdateRequest.objects.all()
    print(obj)
    print(request.method)
    #returning dictionary
    return render(request,'LOR/request_page.html',{"objs ": obj})
