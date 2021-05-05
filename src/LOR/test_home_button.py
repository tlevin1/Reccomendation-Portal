from django.test import TestCase, Client
from Authentication.models import LorUser as User
from LOR.models import LOR


class WriterViewTest(TestCase):

   @classmethod
   def setUpTestData(cls):
       # Create 3 letters of recommendation, 2 for the same writer
       LOR.objects.create(requester='r1', requester_email='r1@umbc.edu', request_date='2021-02-15',
                          position='SWE', writer_email='w1@umbc.edu',
                          due_date='2021-03-30', company_name='FB',
                          company_website='fb.com', company_email='info@fb.com',
                          company_recipients='Sally Hire', status='Pending', cv='tbd',
                          resume='tbd', transcript='tbd', additional_info='none')

       LOR.objects.create(requester='r2', requester_email='r2@umbc.edu', request_date='2021-02-15',
                          position='Intern', writer_email='w3@umbc.edu',
                          due_date='2021-04-10', company_name='nsa', company_website='nsa.gov',
                          company_email='info@nsa.com', company_recipients='Vanessa Hire',
                          status='Accepted', cv='tbd', resume='tbd', transcript='tbd',
                          additional_info='none')

       LOR.objects.create(requester='r3', requester_email='r3@umbc.edu', request_date='2021-02-15',
                          position='Product Manager', writer_email='w1@umbc.edu',
                          due_date='2021-03-10', company_name='Udemy',
                          company_website='udemy.com', company_email='info@udemy.com',
                          company_recipients='Nick Hire', status='Pending', cv='tbd',
                          resume='tbd', transcript='tbd', additional_info='none')

       LOR.objects.create(requester='r3', requester_email='r3@umbc.edu', request_date='2021-02-15',
                          position='SWE Intern', writer_email='w1@umbc.edu',
                          due_date='2021-03-10', company_name='KBR',
                          company_website='kbr.com', company_email='info@kbr.com',
                          company_recipients='Attn: Colin Hire', status='Withdrawn', cv='tbd',
                          resume='tbd', transcript='tbd', additional_info='none')

       # create two users
       w_user1 = User.objects.create_user(username='w_user1', email='w1@umbc.edu', password='justapwd12')
       w_user3 = User.objects.create_user(username='w_user3', email='w3@umbc.edu', password='justapwd12')

       w_user1.save()
       w_user3.save()

   def test_writer_dashboard_home_button(self):
       # Log in the writer
       login = self.client.login(username='w_user1', password='justapwd12')
       sel_box = [1, 3, 4]
       context = {
           "Home": "Home",
           "sel_box": sel_box
       }
       #302 = redirects
       response = self.client.post('/writer/', data=context)
       self.assertEqual(response.status_code, 302)

   def test_writer_dashboard_home_button_does_not_redirect(self):
       # Log in the writer
       login = self.client.login(username='w_user1', password='justapwd12')
       sel_box = [1, 3, 4]
       context = {
           "Home": "Home",
           "sel_box": sel_box
       }
       #302 = redirects
       response = self.client.post('/writer/', data=context)
       self.assertNotEqual(response.status_code, 200)

   def test_requester_dashboard_home_button(self):
       # Log in the requester
       login = self.client.login(username='r_user1', password='justapwd12')
       sel_box = [1, 3, 4]
       context = {
           "Home": "Home",
           "sel_box": sel_box
       }
       #302 = redirects
       response = self.client.post('/requester/', data=context)
       self.assertEqual(response.status_code, 302)

   def test_requester_dashboard_home_button_does_not_redirect(self):
       # Log in the requester
       login = self.client.login(username='r_user1', password='justapwd12')
       sel_box = [1, 3, 4]
       context = {
           "Home": "Home",
           "sel_box": sel_box
       }
       #302 = redirects
       response = self.client.post('/requester/', data=context)
       self.assertNotEqual(response.status_code, 200)

   def test_index_home_page(self):
        client = Client()
        response = client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)

   def test_writer_dashboard_home_button_redirects_to_index(self):
       # Log in the writer
       login = self.client.login(username='w_user1', password='justapwd12')
       sel_box = [1, 3, 4]
       context = {
           "Home": "Home",
           "sel_box": sel_box
       }
       #302 = redirects
       response = self.client.post('/writer/', data=context)
       self.assertEqual(response.status_code, 302)

       response = self.client.post('http://127.0.0.1:8000/', data=context)
       self.assertEqual(response.status_code, 200)

   def test_requester_dashboard_home_button_redirects_to_index(self):
       # Log in the requester
       login = self.client.login(username='r_user1', password='justapwd12')
       sel_box = [1, 3, 4]
       context = {
           "Home": "Home",
           "sel_box": sel_box
       }
       # 302 = redirects
       response = self.client.post('/requester/', data=context)
       self.assertEqual(response.status_code, 302)

       response = self.client.post('http://127.0.0.1:8000/', data=context)
       self.assertEqual(response.status_code, 200)






#



