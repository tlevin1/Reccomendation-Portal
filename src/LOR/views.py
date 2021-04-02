from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from . import models



# stub for home page
def index(writer_rev):
    return HttpResponse('Requests')



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

