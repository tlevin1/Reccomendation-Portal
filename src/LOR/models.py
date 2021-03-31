from django.db import models
from django.utils.timezone import now


#add proffesor in future, right now it is just a sample
Proffesors= [
    ("Professor 1","Dixon"),
    ("Professor 2", "Johnson"),
    ("Professor 2", "Eric"),
]

Status = [
    ("New", "New"),
    ("In Progress","In Progress"),
    ("Finish", "Finish")
]


# Create your models here.
class RequestModel(models.Model):
    requester = models.CharField(max_length=100, blank=False, null=False, default="")
    requester_email = models.EmailField(max_length=200, blank=True, null=True)
    request_date = models.DateField(max_length=100, blank=False, null=False, default=now)
    position = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.DateField(max_length=100, blank=False, null=False)
    writer_name = models.CharField(max_length=100, blank=False, null=False, choices=Proffesors)
    writer_email = models.EmailField(max_length=200, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=False, null=False, default= "")
    company_website = models.URLField(max_length=100, blank=True, null=True)
    company_email = models.EmailField(max_length=100, blank=True, null=True)
    company_recipients = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, blank=False, null=False, choices=Status, default='New')
    cv = models.URLField(max_length=100, blank=True, null=True)
    resume = models.URLField(max_length=100, blank=True, null=True)
    transcript = models.URLField(max_length=100, blank=True, null=True)
    additional_info = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return str(self.requester) + " " + str(self.writer_name) + " " + str(self.status) + " " + str(self.due_date)



class LOR(models.Model):
    requester = models.CharField(max_length=100)
    requester_email = models.EmailField(max_length=100)
    request_date = models.DateField()
    position = models.CharField(max_length=100)
    due_date = models.DateField()
    writer_email = models.EmailField()
    company_name = models.CharField(max_length=100)
    company_website = models.URLField()
    company_email = models.EmailField()
    company_recipients = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    cv = models.TextField()
    resume = models.TextField()
    transcript = models.TextField()
    additional_info = models.TextField()

    def __str__(self):
        return str(self.requester_email) + " " + str(self.writer_email) + " " + str(self.status) \
               + " " + str(self.due_date)

