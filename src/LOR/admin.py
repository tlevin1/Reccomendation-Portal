from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(LOR)
admin.site.register(LorUser)
admin.site.register(LorRequest)
admin.site.register(LorCompanyRecipient)
admin.site.register(LorDocument)
