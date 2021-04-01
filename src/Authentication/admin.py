from django.contrib import admin
from .models import *

#LorUser.objects.get_or_create(username='test1',password=None,email='testp1@umbc.edu')

# Register your models here.
admin.site.register(LorUser)
admin.site.register(LorRequest)
admin.site.register(LorCompanyRecipient)
admin.site.register(LorDocument)