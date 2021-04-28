
from django.test import TestCase
#from django.urls import reverse
#from Authentication.models import LorUser as User
from LOR.models import LOR, Req_a
# from .models import LOR
from LOR.views import writer_req, writer_view, requester_view


class DatabaseTests(TestCase):
    def test_the_basics(self):
        LOR.objects.create(requester='pat', requester_email='pat@umbc.edu', request_date='2021-04-11',
                           position='SWE', writer_email='johnson@umbc.edu',
                           due_date='2021-04-30', company_name='Facebook',
                           company_website='fb.com', company_email='info@fb.com',
                           company_recipients='Sally Hire, John Hire', status='pending', cv='tbd',
                           resume='tbd', transcript='tbd', additional_info='none')

    def test_LOR_string(self):
        lor = LOR(requester_email="pat@umbc.edu", writer_email="johnson@umbc.edu", status="open", due_date="2021-04-26",
                  position="SWE")
        self.assertEqual(str(lor), "pat@umbc.edu bjohnson@umbc.edu open 2021-26-04")