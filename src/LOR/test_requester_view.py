from django.test import TestCase
from django.urls import reverse
from Authentication.models import LorUser as User
from .models import LOR

class RequesterViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 3 letters of recommendation, 2 for the same requester
        LOR.objects.create(requester='r1', requester_email='r1@umbc.edu', request_date='2021-02-15',
                           position='Software Developer', writer_email='w1@umbc.edu',
                           due_date='2021-03-30', company_name='ToysRUs',
                           company_website='toysrus.com', company_email='toysrus@gmail.com',
                           company_recipients='John Day, Sue Night', status='pending', cv='tbd',
                           resume='tbd', transcript='tbd', additional_info='none')

        LOR.objects.create(requester='r2', requester_email='r2@umbc.edu', request_date='2021-02-15',
                           position='Research Analyst', writer_email='w3@umbc.edu',
                           due_date='2021-04-10', company_name='nsa', company_website='nsa.gov',
                           company_email='nsahr@gmail.com', company_recipients='New Hire Staff',
                           status='accepted', cv='tbd', resume='tbd', transcript='tbd',
                           additional_info='none')

        LOR.objects.create(requester='r1', requester_email='r1@umbc.edu', request_date='2021-02-15',
                           position='Project Director', writer_email='w1@umbc.edu',
                           due_date='2021-03-10', company_name='praxis',
                           company_website='praxis.com', company_email='praxis@yahoo.com',
                           company_recipients='Attn: Ronald Menser', status='pending', cv='tbd',
                           resume='tbd', transcript='tbd', additional_info='none')

        # create two users
        r_user1 = User.objects.create_user(username='r_user1', email='r1@umbc.edu', password='justapwd12')
        r_user2 = User.objects.create_user(username='r_user2', email='r2@umbc.edu', password='justapwd12')

        r_user1.save()
        r_user2.save()

    def test_view_url_is_at_correct_location(self):
        # Log in the first writer
        login = self.client.login(username='r_user1', password='justapwd12')
        response = self.client.get('/requester/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_redirects_to_home(self):
        # Check redirects to home page if no one is logged in
        response = self.client.get('/requester/')
        self.assertEqual(response.status_code, 302)

    def test_view_url_is_accessible_by_name(self):
        # Log in the first writer
        login = self.client.login(username='r_user1', password='justapwd12')
        response = self.client.get(reverse('requester_view'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        # Log in the first writer
        login = self.client.login(username='r_user1', password='justapwd12')
        response = self.client.get(reverse('requester_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'requester_view.html')

    def test_view_has_writer_specific_sorted_data(self):
        # Log in the first writer
        login = self.client.login(username='r_user1', password='justapwd12')
        response = self.client.get(reverse('requester_view'))

        # Check that our writer is logged in
        self.assertEqual(str(response.context['user']), 'r_user1')

        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check that we got two requests for the writer
        self.assertTrue(len(response.context['sorted_lors']) == 2)

        # Check that the requests are in sorted order by due date
        last_date = 0
        for lor in response.context['sorted_lors']:
            if last_date == 0:
                last_date = lor.due_date
            else:
                self.assertTrue(last_date <= lor.due_date)
                last_date = lor.due_date