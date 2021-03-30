from django.test import TestCase
from datetime import datetime, timedelta
from .models import *

class LORRoleModelTest(TestCase):
    date_now = datetime.now()
    date_future = date_now + timedelta(days=30)

    @classmethod
    def setUpTestData(cls):
        LorUser.objects.create(first_name='admin', email='adminperson@umbc.edu', role='AD', position="student")
        LorUser.objects.create(name_title='Dr', first_name='Harriet', last_name='Tubman', email='htubman@umbc.edu', role='WR', position="abolitionist")
        LorUser.objects.create(name_title='Dr', first_name='Katherine', last_name='Johnson', email='kjohnson@umbc.edu', role='WR', position="mathematician")
        LorUser.objects.create(first_name='Bob', email='bob@umbc.edu', role='RQ', position="student")
        LorUser.objects.create(first_name='John', email='john@umbc.edu', role='RQ', position="alumni")

    def test_users_exist(self):
        admin = LorUser.objects.get(email='adminperson@umbc.edu')
        writer = LorUser.objects.get(email='htubman@umbc.edu')
        requester = LorUser.objects.get(email='john@umbc.edu')
        self.assertEqual(str(admin.role), "AD")
        self.assertEqual(str(writer.first_name), "Harriet")
        self.assertEqual(str(requester.role), "RQ")

    def test_add_requests(self):
        writer = LorUser.objects.get(email='kjohnson@umbc.edu')
        requester = LorUser.objects.get(email='bob@umbc.edu')

        bobs_request = LorRequest.objects.create(
            request_name = 'myfirstjob',
            request_initial_date = self.date_now,
            request_final_date = self.date_future,
            requester = requester,
            writer = writer
        )

        self.assertEqual(bobs_request.request_initial_date, self.date_now)
        self.assertEqual(bobs_request.writer, writer)

    def test_add_documents(self):
        writer = LorUser.objects.get(email='kjohnson@umbc.edu')
        requester = LorUser.objects.get(email='bob@umbc.edu')
        bobs_request = LorRequest.objects.create(
            request_name='myfirstjob',
            request_initial_date=self.date_now,
            request_final_date=self.date_future,
            requester=requester,
            writer=writer
        )

        LorDocument.objects.create(
            document_name = 'it certification',
            document_type = 'AI',
            request_document = "https://drive.google.com/1234",
            request = bobs_request
        )
        LorDocument.objects.create(
            document_name='my frontend resume',
            document_type = 'RE',
            request_document = "https://drive.google.com/5678",
            request = bobs_request
        )

        bobs_request_documents = LorDocument.objects.filter(request = bobs_request)

        self.assertEqual(bobs_request_documents[0].document_type, 'AI')
        self.assertEqual(bobs_request_documents[1].request_document, "https://drive.google.com/5678")

    def test_add_recipients(self):
        writer = LorUser.objects.get(email='htubman@umbc.edu')
        requester = LorUser.objects.get(email='john@umbc.edu')
        johns_request = LorRequest.objects.create(
            request_name='govt internship',
            request_initial_date=self.date_now,
            request_final_date=self.date_future,
            requester=requester,
            writer=writer
        )

        LorCompanyRecipient.objects.create(
            recipient_name='Barack Obama',
            company_name='US GOVT',
            company_website="https://www.whitehouse.gov/",
            company_email='bobama@us.gov',
            request=johns_request
        )

        LorCompanyRecipient.objects.create(
            recipient_name='Joe Biden',
            company_name='US GOVT',
            company_website="https://www.whitehouse.gov/",
            company_email='jbiden@us.gov',
            request=johns_request
        )

        jhons_request_recipients = LorCompanyRecipient.objects.filter(request = johns_request)

        self.assertEqual(jhons_request_recipients[0].recipient_name, 'Barack Obama')
        self.assertEqual(jhons_request_recipients[1].company_email, 'jbiden@us.gov')