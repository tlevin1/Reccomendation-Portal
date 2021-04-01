from django.contrib import admin
from .models import RequestModel, LOR, Req_a
from .models import RequestModel

# Register your models here.
admin.site.register(LOR)
admin.site.register(RequestModel)
admin.site.register(Req_a)