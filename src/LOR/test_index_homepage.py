from django.test import TestCase, Client
from django.urls import reverse, resolve
from Authentication.models import LorUser as User
from LOR.models import LOR


class Index_HomePageTest(TestCase):

   @classmethod
   def setUpTestData(cls):
       # Create 4 letters of recommendation, user1 has 2 requests and 1 writer action
       LOR.objects.create(requester='user1', requester_email='user1@umbc.edu', request_date='2021-02-15',
                          position='Software Developer', writer_email='w1@umbc.edu',
                          due_date='2021-03-30', company_name='ToysRUs',
                          company_website='toysrus.com', company_email='toysrus@gmail.com',
                          company_recipients='John Day, Sue Night', status='Pending', cv='tbd',
                          resume='tbd', transcript='tbd', additional_info='none')

       LOR.objects.create(requester='user2', requester_email='r2@umbc.edu', request_date='2021-02-15',
                          position='Research Analyst', writer_email='w3@umbc.edu',
                          due_date='2021-04-10', company_name='nsa', company_website='nsa.gov',
                          company_email='nsahr@gmail.com', company_recipients='New Hire Staff',
                          status='Accepted', cv='tbd', resume='tbd', transcript='tbd',
                          additional_info='none')

       LOR.objects.create(requester='user1', requester_email='user1@umbc.edu', request_date='2021-02-15',
                          position='Project Director', writer_email='w2@umbc.edu',
                          due_date='2021-03-10', company_name='praxis',
                          company_website='praxis.com', company_email='praxis@yahoo.com',
                          company_recipients='Attn: Ronald Menser', status='Pending', cv='tbd',
                          resume='tbd', transcript='tbd', additional_info='none')

       LOR.objects.create(requester='r2', requester_email='r2@umbc.edu', request_date='2021-02-15',
                          position='Project Director', writer_email='user1@umbc.edu',
                          due_date='2021-03-10', company_name='praxis',
                          company_website='praxis.com', company_email='praxis@yahoo.com',
                          company_recipients='Attn: Ronald Menser', status='Withdrawn', cv='tbd',
                          resume='tbd', transcript='tbd', additional_info='none')

       # create a user for above data (2 requests, 1 writer action)
       user1 = User.objects.create_user(username='user1', email='user1@umbc.edu', password='justapwd12')
       user1.save()


   def test_index_homepage_url_is_at_correct_location(self):
       # Log in as user1
       login = self.client.login(username='user1', password='justapwd12')
       response = self.client.get('')   # or ('/') ?
       self.assertEqual(response.status_code, 200)


   def test_index_homepage_url_is_accessible_by_name(self):
       # Log in as user1
       login = self.client.login(username='user1', password='justapwd12')
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)


   def test_index_homepage_uses_correct_template(self):
       # Log in as user1
       login = self.client.login(username='user1', password='justapwd12')
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, 'index.html')


   # def test_index_homepage_links_to_dashboards(self):
       # Log in as user1
       # login = self.client.login(username='user1', password='justapwd12')
       # response = self.client.get(reverse('index'))
       # self.assertEqual(response.status_code, 200)

       # self.assertContains(response, 'Requester Dashboard' % reverse("requester_view"))
       # self.assertContains(response, 'Writer Dashboard' % reverse("writer_view"))
       #link = '<a href="%s">Requester Dashboard</a>' % reverse("requester_view")

       # self.assertContains(response, 'href="{% url "requester_view" %}">Requester Dashboard')
       # self.assertContains(response, 'href="{% url "writer_view" %}">Writer Dashboard')


   def test_index_homepage_no_stats_if_not_logged_in(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
       self.assertTrue(response.context['numRequests'] == -1)
       self.assertTrue(response.context['numActions'] == -1)
       # self.assertNotContains(response, 'Your requests:')
       # self.assertNotContains(response, 'Your writer actions:')


   def test_index_homepage_stats_if_logged_in(self):
       # Log in as user1
       login = self.client.login(username='user1', password='justapwd12')
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
       self.assertTrue(response.context['numRequests'] == 2)
       self.assertTrue(response.context['numActions'] == 1)
       # self.assertNotContains(response, 'Your requests:')
       # self.assertNotContains(response, 'Your writer actions:')