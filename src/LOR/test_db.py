
from django.test import TestCase
from LOR.models import LOR, Req_a
from LOR.views import writer_req, writer_view, requester_view
from django.contrib.auth.models import User
from django.test.client import Client
from Authentication.models import LorUser as User
from Authentication.models import UserRoles



class DatabaseTests(TestCase):
    def add_data(self):
        LOR.objects.create(requester='pat', requester_email='pat@umbc.edu', request_date='2021-04-11',
                           position='SWE', writer_email='johnson@umbc.edu',
                           due_date='2021-04-30', company_name='Facebook',
                           company_website='fb.com', company_email='info@fb.com',
                           company_recipients='Sally Hire, John Hire', status='pending', cv='tbd',
                           resume='tbd', transcript='tbd', additional_info='none')


    def test_LOR_string(self):
        lor = LOR(requester_email="pat@umbc.edu", writer_email="bjohnson@umbc.edu", status="open", due_date="2021-04-26",
                  position="SWE")
        self.assertEqual(str(lor), "pat@umbc.edu bjohnson@umbc.edu open 2021-04-26")

    def test_new_writer_created(self):
        #create new super user
        password = 'pass'
        admin = User.objects.create_superuser('super','super@test.umbc.com', password)
        self.client.login(username = admin.username, password = password)
        #check
        self.assertEqual(str(password),'pass')

    def test_new_writer_created_that_is_not_super_user(self):
        #non super user
        password = 'pass'
        admin = User.objects.create_user('nonsuper','nonsuper@test.umbc.com', password)
        self.client.login(username = admin.username, password = password)
        #check
        self.assertEqual(str(password),'pass')

    def get_number_of_writers_that_are_users(self):
        num_writers = len(User.objects.filter(role=UserRoles.WRITER))
        self.assertEqual(1, num_writers)

    def get_number_of_admins(self):
        admin_num = len(User.objects.filter(role=UserRoles.ADMIN))
        self.assertEqual(1, admin_num)

    def get_number_of_requests(self):
        requests_num = len(User.objects.filter(role=UserRoles.REQUESTER))
        self.assertEqual(1, requests_num)

    def test_get_writers_name(self):
        writer_first_name = User.objects.filter(role=UserRoles.WRITER).first()
        writer_last_name = User.objects.filter(role=UserRoles.WRITER, first_name='Admin').first()
        #self.assertEqual(str("Benjamin"), writer_first_name.get_first_name())
        #self.assertEqual(str("Johnson"), writer_last_name.get_last_name())

