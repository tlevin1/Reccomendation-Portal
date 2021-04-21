from django.test import TestCase, Client
from django.urls import reverse, resolve
from Authentication.models import LorUser as User
from datetime import datetime
from .models import LOR, Req_a
from .views import writer_req

class WriterViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 3 letters of recommendation, 2 for the same writer
        LOR.objects.create(requester='r1', requester_email='r1@umbc.edu', request_date='2021-02-15',
                           position='Software Developer', writer_email='w1@umbc.edu',
                           due_date='2021-03-30', company_name='ToysRUs',
                           company_website='toysrus.com', company_email='toysrus@gmail.com',
                           company_recipients='John Day, Sue Night', status='Pending', cv='tbd',
                           resume='tbd', transcript='tbd', additional_info='none')

        LOR.objects.create(requester='r2', requester_email='r2@umbc.edu', request_date='2021-02-15',
                           position='Research Analyst', writer_email='w3@umbc.edu',
                           due_date='2021-04-10', company_name='nsa', company_website='nsa.gov',
                           company_email='nsahr@gmail.com', company_recipients='New Hire Staff',
                           status='Accepted', cv='tbd', resume='tbd', transcript='tbd',
                           additional_info='none')

        LOR.objects.create(requester='r3', requester_email='r3@umbc.edu', request_date='2021-02-15',
                           position='Project Director', writer_email='w1@umbc.edu',
                           due_date='2021-03-10', company_name='praxis',
                           company_website='praxis.com', company_email='praxis@yahoo.com',
                           company_recipients='Attn: Ronald Menser', status='Pending', cv='tbd',
                           resume='tbd', transcript='tbd', additional_info='none')

        LOR.objects.create(requester='r3', requester_email='r3@umbc.edu', request_date='2021-02-15',
                           position='Project Director', writer_email='w1@umbc.edu',
                           due_date='2021-03-10', company_name='praxis',
                           company_website='praxis.com', company_email='praxis@yahoo.com',
                           company_recipients='Attn: Ronald Menser', status='Withdrawn', cv='tbd',
                           resume='tbd', transcript='tbd', additional_info='none')

        # create two users
        w_user1 = User.objects.create_user(username='w_user1', email='w1@umbc.edu', password='justapwd12')
        w_user3 = User.objects.create_user(username='w_user3', email='w3@umbc.edu', password='justapwd12')

        w_user1.save()
        w_user3.save()

    def test_view_url_is_at_correct_location(self):
        # Log in the first writer
        login = self.client.login(username='w_user1', password='justapwd12')
        response = self.client.get('/writer/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_redirects_to_home(self):
        # Check redirects to home page if no one is logged in
        response = self.client.get('/writer/')
        self.assertEqual(response.status_code, 302)

    def test_view_url_is_accessible_by_name(self):
        # Log in the first writer
        login = self.client.login(username='w_user1', password='justapwd12')
        response = self.client.get(reverse('writer_view'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        # Log in the first writer
        login = self.client.login(username='w_user1', password='justapwd12')
        response = self.client.get(reverse('writer_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'writer_view.html')

    def test_view_has_writer_specific_sorted_data(self):
        # Log in the first writer
        login = self.client.login(username='w_user1', password='justapwd12')
        response = self.client.get(reverse('writer_view'))

        # Check that our writer is logged in
        self.assertEqual(str(response.context['user']), 'w_user1')

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


    def test_accept_button(self):
        # Log in the first writer
        login = self.client.login(username='w_user1', password='justapwd12')
        sel_box = [1, 3, 4]
        context = {
            "Accept": "Accept",
            "sel_box": sel_box
        }
        response = self.client.post('/writer/', data=context)
        self.assertEqual(response.status_code, 200)

        # test error msg is sent if attempting to accept a completed or withdrawn request
        self.assertContains(response, 'Unable to accept a completed or withdrawn request')

        # test that request can be accepted (id=1 has valid Pending status)
        lor = LOR.objects.get(id=sel_box[0])
        self.assertEqual(lor.status, "Accepted")

        # test that request can be accepted (id=3 has valid Pending status)
        lor = LOR.objects.get(id=sel_box[2])
        self.assertEqual(lor.status, "Accepted")

    def test_complete_button(self):
        # Log in the first writer
        login = self.client.login(username='w_user1', password='justapwd12')
        sel_box = [1, 3, 4]
        context = {
            "Complete": "Complete",
            "sel_box": sel_box
        }
        response = self.client.post('/writer/', data=context)
        self.assertEqual(response.status_code, 200)

        # test error msg is sent if attempting to complete a withdrawn or denied request
        self.assertContains(response, 'Unable to complete a withdrawn or denied request')

        # test that request can be completed (id=1 has valid Pending status)
        lor = LOR.objects.get(id=sel_box[0])
        self.assertEqual(lor.status, "Completed")

        # test that request can be completed (id=3 has valid Pending status)
        lor = LOR.objects.get(id=sel_box[2])
        self.assertEqual(lor.status, "Completed")


    def test_deny_button(self):
        # Log in the first writer
        login = self.client.login(username='w_user1', password='justapwd12')
        sel_box = [1, 3, 4]
        context = {
            "Deny": "Deny",
            "sel_box": sel_box
        }
        response = self.client.post('/writer/', data=context)
        self.assertEqual(response.status_code, 200)

        # test error msg is sent if attempting to deny a withdrawn or completed request
        self.assertContains(response, 'Unable to deny a withdrawn or completed request')

        # test that request can be denied (id=1 has valid Pending status)
        lor = LOR.objects.get(id=sel_box[0])
        self.assertEqual(lor.status, "Denied")

        # test that request can be denied (id=3 has valid Pending status)
        lor = LOR.objects.get(id=sel_box[2])
        self.assertEqual(lor.status, "Denied")


class TestViews(TestCase):


    def test_project_Req(self):
        self.client = Client()
        self.req_url = reverse('writer_req')

        response = self.client.get(reverse('writer_req'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'LOR/requests.html')
    #testing to see if there is a 200 response
    def test_project_accept_post(self):
        self.req = Req_a.objects.create(
        name= 'thuan',
        answer = '',
        R_date = '2001-02-12',
        A_date = datetime.now()
        )

        response = self.client.post(reverse('writer_req'), {
            'name' : 'thuan',
            'answer' : '',
            'R_date' : '2001-05-03',
            'A_date' : '2000-03-21'
        })
        self.assertEquals(response.status_code, 200)
        #testing to see if Post was succesful
        self.assertEquals(self.req.name, 'thuan')
        #testing to see if variable are still correct

class TestURL(TestCase):

    def test_requests_url(self):
        url = reverse('writer_req')
        self.assertEqual(resolve(url).func, writer_req)
        #test to see if it is correct url
