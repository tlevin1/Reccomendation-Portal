from django.db import models
from django.utils.timezone import now
from datetime import datetime

# Create your models here.
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
        return str(self.requester) + " " + "\n" + str(self.position) + " " + "\n" + str(self.due_date) + " " + "\n" + str(self.request_date) + " " + "\n" + str(self.writer_email) + " " + "\n" + str(self.company_name) + " " + "\n" + str(self.company_website) + " " + "\n" + str(self.company_recipients)