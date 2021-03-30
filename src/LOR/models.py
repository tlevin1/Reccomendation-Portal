from django.db import models
from django.utils.translation import gettext_lazy as gettextlazy

'''
    User Roles
    AD ADMIN
    WR WRITER
    RQ REQUESTER
'''

'''
    Document Types
    RE RESUME
    TR TRANSCRIPT
    CV COVERLETTER
    AI ADDITIONALINFO
'''


class UserRoles(models.TextChoices):
    ADMIN = 'AD', gettextlazy('Admin')
    WRITER = 'WR', gettextlazy('Writer')
    REQUESTER = 'RQ', gettextlazy('Requester')


class DocumentTypes(models.TextChoices):
    RESUME = 'RE', gettextlazy('Resume')
    TRANSCRIPT = 'TR', gettextlazy('Transcript')
    COVERLETTER = 'CV', gettextlazy('CoverLetter')
    ADDITIONALINFO = 'AI', gettextlazy('AdditionalInfo')


class LorUser(models.Model):
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    name_title = models.CharField(max_length=25)
    role = models.CharField(max_length=2,choices=UserRoles.choices,
                            default=UserRoles.REQUESTER)
    position = models.CharField(max_length=100)


class LorRequest(models.Model):
    request_name = models.CharField(max_length=100)
    request_initial_date = models.DateField()
    request_final_date = models.DateField()
    requester = models.ForeignKey(LorUser, related_name="related_requester_id", on_delete=models.CASCADE)
    writer = models.ForeignKey(LorUser, related_name="related_writer_id", on_delete=models.CASCADE)


class LorCompanyRecipient(models.Model):
    recipient_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_website = models.URLField()
    company_email = models.EmailField()
    request = models.ForeignKey(LorRequest, related_name="related_recipient_request_id", on_delete=models.CASCADE)


class LorDocument(models.Model):
    document_name = models.CharField(max_length=100)
    document_type = models.CharField(max_length=2,choices=DocumentTypes.choices,
                                     default=DocumentTypes.ADDITIONALINFO)
    request_document = models.TextField()
    request = models.ForeignKey(LorRequest, related_name="related_document_request_id", on_delete=models.CASCADE)


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
        return str(self.requester_email) + " " + str(self.writer_email) + " " + str(self.status) + " " + str(self.due_date)
