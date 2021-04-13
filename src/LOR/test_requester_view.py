# from django.test import TestCase, Client
# from django.urls import reverse, resolve
# from Authentication.models import LorUser as User
# from datetime import datetime
# from src.LOR.models import LOR, Req_a
# from src.LOR.views import requester_view
from django.test import TestCase, Client
from django.urls import reverse, resolve
from Authentication.models import LorUser as User
from datetime import datetime
from .models import LOR, Req_a
from .views import writer_req

class RequesterViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Created 2 letters of recommendation
        LOR.objects.create(requester='pat', requester_email='pat@umbc.edu', request_date='2021-04-11',
                           position='SWE', writer_email='johnson@umbc.edu',
                           due_date='2021-04-30', company_name='Facebook',
                           company_website='fb.com', company_email='info@fb.com',
                           company_recipients='Sally Hire, John Hire', status='pending', cv='tbd',
                           resume='tbd', transcript='tbd', additional_info='none')

        LOR.objects.create(requester='dave', requester_email='dave@umbc.edu', request_date='2021-04-15',
                           position='Junior SWE', writer_email='dixion@umbc.edu',
                           due_date='2021-05-10', company_name='Morgan Stanley', company_website='morganstanley.com',
                           company_email='info@ms.com', company_recipients='Morgan Hire',
                           status='accepted', cv='tbd', resume='tbd', transcript='tbd',
                           additional_info='none')

        # create two requester users
        r_user1 = User.objects.create_user(username='r_user1', email='r1@umbc.edu', password='pass1')
        r_user3 = User.objects.create_user(username='r_user3', email='r3@umbc.edu', password='pass2')

        r_user1.save()
        r_user3.save()

    def test_view_url_is_at_correct_location(self):
        # Log in the first requester
        login = self.client.login(username='r_user1', password='pass1')
        response = self.client.get('/req_view/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_redirects_to_home(self):
        # Check redirects to home page if no one is logged in
        response = self.client.get('/req_view/')
        self.assertEqual(response.status_code, 302)

    def test_view_uses_correct_template(self):
        # Log in the first writer
        login = self.client.login(username='r_user1', password='pass1')
        response = self.client.get(reverse('requester_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'requester_view.html')

    def test_view_has_requester_specific_sorted_data(self):
        # Log in the first requester
        login = self.client.login(username='r_user1', password='pass1')
        response = self.client.get(reverse('requester_view'))

        # Check that requester is logged in
        self.assertEqual(str(response.context['user']), 'r_user1')

        # Check that received a response "success"
        self.assertEqual(response.status_code, 200)

        # Check that  two requests
        self.assertTrue(len(response.context['sorted_lors']) == 2)

        # Check that the requests are in sorted order by due date
        last_date = 0
        for lor in response.context['sorted_lors']:
            if last_date == 0:
                last_date = lor.due_date
            else:
                self.assertTrue(last_date <= lor.due_date)
                last_date = lor.due_date
class TestViews(TestCase):


    def test_request_view(self):
        self.client = Client()
        self.req_url = reverse('requester_view')

        response = self.client.get(reverse('requester_view'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'LOR/requester_view.html')
    #testing to see if there is a 200 response

class TestURL(TestCase):

    def test_requester_url(self):
        url = reverse('req_view')
        print((resolve(url)))
        self.assertEqual(resolve(url).func, requester_view)
        #test to see if it is correct url
