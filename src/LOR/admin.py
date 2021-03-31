from django.contrib import admin

from .models import RequestModel, LOR

# Register your models here.
admin.site.register(LOR)
admin.site.register(RequestModel)
