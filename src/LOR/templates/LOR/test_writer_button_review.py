from .models import Req_a
from .views import writer_req
from django.urls import reverse, resolve
from Authentication.models import LorUser as User
from datetime import datetime
from .models import LOR, Req_a
from LOR.models import LOR


class WriterViewButtonTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create LOR
        LOR.objects.create(requester='req1', requester_email='req1@umbc.edu', request_date='2021-03-11',
                           position='SWE', writer_email='wr1@umbc.edu',
                           due_date='2021-01-22', company_name='Google',
                           company_website='google.com', company_email='info@google.com',
                           company_recipients='Katherine H, Katniss Everdeen', status='New', cv='tbd',
                           resume='tbd', transcript='tbd', additional_info='none')

        LOR.objects.create(requester='req2', requester_email='req2@umbc.edu', request_date='2021-01-19',
                           position='SWE Intern', writer_email='wr2@umbc.edu',
                           due_date='2021-01-15', company_name='Amazon', company_website='amazon.com',
                           company_email='info@amazon.com', company_recipients='Sally Amazon',
                           status='Accepted', cv='tbd', resume='tbd', transcript='tbd',
                           additional_info='Hey!')

        LOR.objects.create(requester='req3', requester_email='req3@umbc.edu', request_date='2021-01-01',
                           position='Product Manager', writer_email='wr1@umbc.edu',
                           due_date='2021-03-13', company_name='Udemy',
                           company_website='udemy.com', company_email='info@udemy.com',
                           company_recipients='Sally Udemy', status='Pending', cv='tbd',
                           resume='tbd', transcript='tbd', additional_info='none')

    def test_login_as_admin(self):
        # Log in as admin
        login = self.client.login(username='admin', password='pass')
        response = self.client.get('/writer/')
        self.assertEqual(response.status_code, 200)

    def test_login_as_writer(self):
        # Log in as writer
        login = self.client.login(username='bjohnson', password='passb')
        response = self.client.get('/writer/')
        self.assertEqual(response.status_code, 200)

    def test_review_button(self):
        # Log in
        login = self.client.login(username='wr1', password='pass')
        #check box selected
        sel_box = [1, 3, 4]
        context = {
            "sel_box": sel_box,
            "Review": "Review"

        }
        response = self.client.post('/writer/', data=context)
        self.assertEqual(response.status_code, 200)

    def test_select_review_button(self):
        # Log in
        login = self.client.login(username='wr2', password='pass')
        #check box selected
        sel_box = [1, 2, 4]
        context = {
            "sel_box": sel_box,
            "Review": "Review"

        }
        response = self.client.post('/writer/', data=context)
        self.assertEqual(response.status_code, 200)