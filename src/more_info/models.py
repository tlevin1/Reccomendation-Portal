from django.db import models
from django.utils import timezone
# Create your models here.
class moreinfo(models.Model):
    name = models.CharField(max_length=100)
    send_to= models.CharField(max_length=100,blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=100)



    def __str__(self):
        return self.name
    #this model will be use