from django.test import TestCase
from LOR.form import RequestForm


# Create your tests here.
class LORModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form1 = RequestForm(data={
            'requester': "Bob",
            'requester_email': 'b@umbc.edu',
            'position': 'developer',
            'due_date': '09/09/09',
            'writer_name': 'Dixon',
            'company_name': 'NSA',
        })

    def test_form_invalid_data(self):
        self.assertFalse(self.form1.is_valid())
