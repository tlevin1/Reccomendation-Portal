from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LOR


# stub for home page
def index(writerrev):
    return HttpResponse('Requests')


# display table of writer actions
# actions are: accept, deny, review, complete

@login_required

def writer_review(writerrev):
    print(writerrev.method)
    cur_user = writerrev.user
    print(cur_user)
    print("User is ", cur_user)

    # Make sure user is logged in
    if cur_user.is_authenticated:
        print("User is logged in")
        if writerrev.method == 'POST':
            # Get the list of ids associated with selected table rows
            if not writerrev.POST.getlist('sel_box'):
                # messages.info(request, 'Nothing Selected')
                print('Nothing selected')
            else:
                sel_ids = writerrev.POST.getlist('sel_box')
                # Check which button is pressed
                if 'Cover Letter' in writerrev.POST:
                    print('Cover Letter Button pressed')
                elif 'Resume' in writerrev.POST:
                    print('Resume Button pressed')
                elif 'Unnoficial Transcript' in writerrev.POST:
                    print('Unnoficial Transcript Button pressed')
                elif 'Additional Information' in writerrev.POST:
                    print('Review Button pressed')
        sorted_lors = LOR.objects.filter(writer_email=cur_user.email).order_by("due_date")
        context = {"sorted_lors": sorted_lors}
        return render(writerrev, 'writer_review.html', context)
    else:
        # If no one is logged in, send back to home page
        return redirect('/')