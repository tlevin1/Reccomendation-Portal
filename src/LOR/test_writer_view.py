from django.test import TestCase
from django.urls import reverse

from .models import LOR


class AuthorListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 3 letters of recommendation, 2 for the same writer
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

        LOR.objects.create(requester='r3', requester_email='r3@umbc.edu', request_date='2021-02-15',
                           position='Project Director', writer_email='w1@umbc.edu',
                           due_date='2021-03-10', company_name='praxis',
                           company_website='praxis.com', company_email='praxis@yahoo.com',
                           company_recipients='Attn: Ronald Menser', status='pending', cv='tbd',
                           resume='tbd', transcript='tbd', additional_info='none')

    def test_view_url_is_at_correct_location(self):
        response = self.client.get('/writer/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_is_accessible_by_name(self):
        response = self.client.get(reverse('writer_view'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('writer_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'writer_view.html')

    def test_view_has_all_data(self):
        response = self.client.get(reverse('writer_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['lors']) == 3)
