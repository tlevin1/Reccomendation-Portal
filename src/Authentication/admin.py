from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

#add sample users

# Register your models here.
admin.site.register(LorUser)
admin.site.register(LorRequest)
admin.site.register(LorCompanyRecipient)
admin.site.register(LorDocument)