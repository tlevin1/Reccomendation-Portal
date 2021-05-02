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
                           company_recipients='John Day, Sue Night', status='Pending', cv='tbd',
                           resume='tbd', transcript='tbd', additional_info='none')

        LOR.objects.create(requester='r2', requester_email='r2@umbc.edu', request_date='2021-02-15',
                           position='Research Analyst', writer_email='w3@umbc.edu',
                           due_date='2021-04-10', company_name='nsa', company_website='nsa.gov',
                           company_email='nsahr@gmail.com', company_recipients='New Hire Staff',
                           status='Accepted', cv='tbd', resume='tbd', transcript='tbd',
                           additional_info='none')

        LOR.objects.create(requester='r1', requester_email='r1@umbc.edu', request_date='2021-02-15',
                           position='Project Director', writer_email='w1@umbc.edu',
                           due_date='2021-03-10', company_name='praxis',
                           company_website='praxis.com', company_email='praxis@yahoo.com',
                           company_recipients='Attn: Ronald Menser', status='Completed', cv='tbd',
                           resume='tbd', transcript='tbd', additional_info='none')

        # create two users
        r_user1 = User.objects.create_user(username='r_user1', email='r1@umbc.edu', password='justapwd12')
        r_user2 = User.objects.create_user(username='r_user2', email='r2@umbc.edu', password='justapwd12')

        r_user1.save()
        r_user2.save()

    def test_view_url_is_at_correct_location(self):
        # Log in the first requester
        login = self.client.login(username='r_user1', password='justapwd12')
        response = self.client.get('/requester/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_redirects_to_home(self):
        # Check redirects to home page if no one is logged in
        response = self.client.get('/requester/')
        self.assertEqual(response.status_code, 302)

    def test_view_url_is_accessible_by_name(self):
        # Log in the first requester
        login = self.client.login(username='r_user1', password='justapwd12')
        response = self.client.get(reverse('requester_view'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        # Log in the first requester
        login = self.client.login(username='r_user1', password='justapwd12')
        response = self.client.get(reverse('requester_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'requester_view.html')

    def test_view_has_requester_specific_sorted_data(self):
        # Log in the first requester
        login = self.client.login(username='r_user1', password='justapwd12')
        response = self.client.get(reverse('requester_view'))

        # Check that our requester is logged in
        self.assertEqual(str(response.context['user']), 'r_user1')

        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check that we got two requests for the requester
        self.assertTrue(len(response.context['sorted_lors']) == 2)

        # Check that the requests are in sorted order by due date
        last_date = 0
        for lor in response.context['sorted_lors']:
            if last_date == 0:
                last_date = lor.due_date
            else:
                self.assertTrue(last_date <= lor.due_date)
                last_date = lor.due_date


    def test_nothing_selected(self):
        # test if no selections made in requester dashboard
        login = self.client.login(username='r_user1', password='justapwd12')
        sel_box = []
        response = self.client.post('/requester/', data={"sel_box": sel_box})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nothing selected')


    def test_withdraw(self):
        login = self.client.login(username='r_user1', password='justapwd12')
        sel_box = [1, 3]
        context = {
            "Withdraw": "Withdraw",
            "sel_box": sel_box
        }
        response = self.client.post('/requester/', data=context)
        self.assertEqual(response.status_code, 200)

        # test error msg is sent if attempting to withdraw a completed request
        self.assertContains(response, 'Unable to withdraw a completed request')

        # test that request can be withdrawn (id=1 has valid Pending status)
        lor = LOR.objects.get(id=sel_box[0])
        self.assertEqual(lor.status, "Withdrawn")

    def test_review_multiple_requests(self):
        login = self.client.login(username='r_user1', password='justapwd12')
        sel_box = [1, 3]
        context = {
            "Review": "Review",
            "sel_box": sel_box
        }

        response = self.client.post('/requester/', data=context)
        self.assertEqual(response.status_code, 200)

        #test error message is sent if attempting to review more than one request
        self.assertContains(response, 'Please only select one request to review/update')

    def test_review_single_request(self):
        login = self.client.login(username='r_user1', password='justapwd12')
        sel_box = [1]
        context = {
            "Review": "Review",
            "sel_box": sel_box
        }

        response = self.client.post('/requester/', data=context)
        self.assertEqual(response.status_code, 200)

        # verify correct template is displayed
        self.assertTemplateUsed(response, 'updateLOR.html')

    def test_request_is_updated(self):
        login = self.client.login(username='r_user1', password='justapwd12')
        sel_box = [1]
        context = {
            "id": 1,
            "position": "Analyst",
            "due_date": "2021-12-25",
            "additional_info": "tbd",
            "company_name": "ToysRUs",
            "company_website": "toysrus.com",
            "company_email": "toysrus@gmail.com",
            "company_recipients": "John Day, Sue Night",
            "cv": "tbd",
            "resume": "tbd",
            "transcript": "tbd"
        }

        response = self.client.post('/updateLOR/', data=context)
        lor = LOR.objects.get(id=1)
        self.assertEqual(lor.position, "Analyst")
        self.assertEqual(lor.additional_info, "tbd")
        self.assertEqual(lor.company_name, "ToysRUs")
        self.assertEqual(lor.company_website, "toysrus.com")
        self.assertEqual(lor.company_email, "toysrus@gmail.com")
        self.assertEqual(lor.company_recipients, "John Day, Sue Night")
        self.assertEqual(lor.cv, "tbd")
        self.assertEqual(lor.resume, "tbd")
        self.assertEqual(lor.transcript, "tbd")