from django.db import models


# Create your models here.
class LOR(models.Model):
    name = models.CharField(max_length=100)
    requester = models.CharField(max_length=100)
    request_date = models.DateField()
    position = models.CharField(max_length=100)
    due_date = models.DateField()
    writer = models.EmailField()
    company_name = models.CharField(max_length=100)
    company_website = models.CharField(max_length=100)
    company_email = models.EmailField()
    company_recipients = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    cv = models.TextField()
    resume = models.TextField()
    transcript = models.TextField()
    additional_info = models.TextField()
