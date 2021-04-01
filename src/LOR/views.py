from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import LOR


# stub for home page
def index(writerrev):
    return HttpResponse('Requests')

#display id of user
# display table of writer actions
# actions are: accept, deny, review, complete


def writer_review(sel_ids):
    for id in sel_ids:
        print(id)

@login_required
def writer_view(writerrev):
    print(writerrev.method)
    cur_user = writerrev.user
    print(cur_user)
    print("User is ", cur_user)

    if writerrev.method == 'POST':
        if not writerrev.POST.getlist('sel_box'):
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
                elif 'Next' in writerrev.POST:
                    print('Next Button pressed')
        sorted_lors = LOR.objects.filter(writer_email=cur_user.email).order_by("due_date")
        context = {"sorted_lors": sorted_lors}
        return render(writerrev, 'LOR/writer_view.html', context)
        #return render(writerrev, 'writer_review.html', context)
    else:
        # If no one is logged in, send back to home page
        return redirect('/')