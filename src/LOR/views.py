from django.shortcuts import render
from django.http import HttpResponse
from .models import LOR


# stub for home page
def index(request):
    return HttpResponse('Letters of Recommendation index')


# display table of writer actions
# actions are: accept, deny, review, complete
def writer_view(request):
    print(request.method)
    lors = LOR.objects.all()
    context = {"lors": lors}
    return render(request, 'writer_view.html', context)

