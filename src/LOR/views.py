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
    sorted_lors = LOR.objects.all().order_by("due_date")
    context = {"sorted_lors": sorted_lors}
    return render(request, 'writer_view.html', context)


