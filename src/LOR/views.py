from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LOR


# stub for home page
def index(writer):
    return HttpResponse('Requests')


# display table of writer actions
# actions are: accept, deny, review, complete
def writer_view(writer):
    print(writer.method)
    cur_user = writer.user
    print(cur_user)
    print("User is ", cur_user)

    # Make sure user is logged in
    if cur_user.is_authenticated:
        print("User is logged in")
        if writer.method == 'POST':
            # Get the list of ids associated with selected table rows
            if not writer.POST.getlist('sel_box'):
                # messages.info(request, 'Nothing Selected')
                print('Nothing selected')
            else:
                sel_ids = writer.POST.getlist('sel_box')
                # Check which button is pressed
                if 'Cover Letter' in writer.POST:
                    print('Cover Letter Button pressed')
                elif 'Resume' in writer.POST:
                    print('Resume Button pressed')
                elif 'Unnoficial Transcript' in writer.POST:
                    print('Unnoficial Transcript Button pressed')
                elif 'Additional Information' in writer.POST:
                    print('Review Button pressed')
        sorted_lors = LOR.objects.filter(writer_email=cur_user.email).order_by("due_date")
        context = {"sorted_lors": sorted_lors}
        return render(writer, 'writer_view.html', context)
    else:
        # If no one is logged in, send back to home page
        return redirect('/')