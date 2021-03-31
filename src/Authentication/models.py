from django.db import models
from django.utils.translation import gettext_lazy as gettextlazy
from django.contrib.auth.models import User

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
    base_user = models.ForeignKey(User,related_name="related_baseuser_id",
                                  unique=True,on_delete=models.CASCADE);
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    name_title = models.CharField(max_length=25)
    role = models.CharField(max_length=2,choices=UserRoles.choices,
                            default=UserRoles.REQUESTER, )
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
