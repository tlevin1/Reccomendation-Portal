from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .forms import Infoform
from .models import moreinfo

# Create your views here.
def writer_more_info(request):
    if request.method == 'POST':
        form = Infoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('writer_more_info')
        else:
            form = Infoform()

    # check form sending in is valid, and save form if valid

    return render(request, 'more_info/moreinfo.html',{'infoform': Infoform})

def view_more_info(request):
    info = moreinfo.objects.all()

    return render(request, 'more_info/viewmoreinfo.html', {'infos': info})