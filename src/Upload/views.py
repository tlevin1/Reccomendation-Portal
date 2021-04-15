from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .form import Uploadform
from .models import Upload

# Create your views here.
def upload_file(request):

    if request.method == 'POST':
        form = Uploadform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
        else:
            form = Uploadform()
# check form sending in is valid, and save form if valid

    return render(request, 'Upload/upload.html', {'uploadform': Uploadform})


def upload_view(request):
    Uploads = Upload.objects.all()
#show all of the uploads from database
    return render(request, 'Upload/uploadview.html', {'uploads': Uploads})

def delete_upload(request, pk):
    Uploads = Upload.objects.all()
    if request.method == 'POST':
        DEL = Upload.objects.get(pk=pk)
        DEL.delete()
#deleting upload object using pk, allowing writer to delete if they wish to
    return render(request, 'Upload/uploadview.html', {'uploads': Uploads})