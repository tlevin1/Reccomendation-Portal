from django.test import TestCase
#for testing the url
from django.urls import reverse, resolve
from LOR import views

#test html
class LOR_test_url(TestCase):
#test url
    def test_writer_review(self):
        url = reverse('writer_rev/')
        self.assertEqual(resolve(url).func, views.writer_review)

#test data
class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        LOR.objects.create(requester='Abigail', requester_email='amyers@gmail.com', request_date='2021-07-01',
                           position='SWE', due_date='2021-04-08', writer_email='teacher2@gmail.com',
                           company_name='Facebook', company_website='facebook.com', company_email='hr@facebook.com',
                           company_recipients='Sally Hire', status='open', cv='TBD', resume='TBD',
                           transcript='TBD', additional_info='TBD')

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test1(self):
        # Some test using self.foo
        ...

    def test2(self):
        # Some other test using self.foo
        ...

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)