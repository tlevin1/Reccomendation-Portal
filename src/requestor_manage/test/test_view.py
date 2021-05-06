from django.test import TestCase, Client
from django.urls import reverse, resolve
from LOR import models
import json


class requestor_manage_test_view(TestCase):
    def setUp(self):
        self.client = Client()
        self.requesting_url = reverse('request_view')
        self.object1 = models.RequestModel.objects.create(request_date='2021-01-01',
                           position='developer', due_date='2021-02-02',
                           company_name='NSA', company_website='nsa.gov', company_email='nsa@gov.com',
                           company_recipients='julia', status='New', cv='TBD', resume='TBD',
                           transcript='TBD', additional_info='TBD')


    def test_view_enter_request(self):
        response = self.client.post(self.requesting_url,)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'requestor_manage/request_view.html')

    def test_view_enter_request_have_data(self):
        response = self.client.post(self.requesting_url,{
            'requester': "Bob",
            'requester_email': 'b@gmail.com',
            'position': 'developer',
            'due_date': '2021-02-02',
            'writer_name': 'kate',
            'company_name': 'NSA',
            'company_website': 'nsa.gov',
            'company_email': 'nsa@gov.com',
            'company_recipients': 'julia',
            'cv': 'TBD',
            'resume': 'TBD',
            'transcript': 'TBD',
            'additional_info': 'TBD',
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'requestor_manage/request_view.html')
        self.assertEqual(self.object1.position, "developer")
        self.assertEqual(self.object1.due_date, "2021-02-02")
        self.assertEqual(self.object1.company_name, "NSA")
        self.assertEqual(self.object1.company_website, "nsa.gov")
        self.assertEqual(self.object1.company_recipients, "julia")
        self.assertEqual(self.object1.cv, "TBD")
        self.assertEqual(self.object1.resume, "TBD")
        self.assertEqual(self.object1.transcript, "TBD")
        self.assertEqual(self.object1.additional_info, "TBD")

