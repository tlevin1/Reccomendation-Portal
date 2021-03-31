from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

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
    ADMIN = 'AD', _('Admin')
    WRITER = 'WR', _('Writer')
    REQUESTER = 'RQ', _('Requester')


class DocumentTypes(models.TextChoices):
    RESUME = 'RE', _('Resume')
    TRANSCRIPT = 'TR', _('Transcript')
    COVERLETTER = 'CV', _('CoverLetter')
    ADDITIONALINFO = 'AI', _('AdditionalInfo')


class LorUser(AbstractUser):
    name_title = models.CharField(max_length=25,null=True,blank=True)
    role = models.CharField(max_length=2,choices=UserRoles.choices,default=UserRoles.REQUESTER)
    position = models.CharField(max_length=100,null=True, blank=True)
    password = models.CharField(_('password'),max_length=128,null=True,blank=True)


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
