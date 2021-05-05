from django.db import models

# Create your models here.
class Upload(models.Model):
    name = models.CharField(max_length=100)
    send_to = models.CharField(max_length=100, null=False, blank=True)
    type = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='Upload/pdf/')

    def __str__(self):
        return self.name
    #this model will be use to implement an upload form, user need to enter name, type of document, and actual pdf