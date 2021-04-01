from django.test import TestCase
from .models import LOR



# Create your tests here.
class LORModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        LOR.objects.create(requester='Bob', requester_email='b@gmail.com', request_date='2021-01-01',
                           position='developer', due_date='2021-02-02', writer_email='k@umbc.edu',
                           company_name='NSA', company_website='nsa.gov', company_email='nsa@gov.com',
                           company_recipients='julia', status='pending', cv='TBD', resume='TBD',
                           transcript='TBD', additional_info='TBD')

    def test_good_to_string(self):
        lor = LOR(requester_email="b@gmail.com", writer_email="k@umbc.edu", status="pending", due_date="2021-01-01",
                  position="developer")
        self.assertEqual(str(lor), "b@gmail.com k@umbc.edu pending 2021-01-01")

    def test_requester_label(self):
        lor = LOR.objects.get(id=1)
        field_label = lor._meta.get_field('requester').verbose_name
        self.assertEqual(field_label, 'requester')

    def test_requester_max_len(self):
        lor = LOR.objects.get(id=1)
        max_len = lor._meta.get_field('requester').max_length
        self.assertEqual(max_len, 100)

    def test_requester_email(self):
        lor = LOR.objects.get(id=1)
        field_label = lor._meta.get_field('requester_email').verbose_name
        self.assertEqual(field_label, 'requester email')

    def test_request_date(self):
        lor = LOR.objects.get(id=1)
        field_label = lor._meta.get_field('request_date').verbose_name
        self.assertEqual(field_label, 'request date')

    def test_positon(self):
        lor = LOR.objects.get(id=1)
        field_label = lor._meta.get_field('position').verbose_name
        self.assertEqual(field_label, 'position')

    def test_position_max_len(self):
        lor = LOR.objects.get(id=1)
        max_len = lor._meta.get_field('position').max_length
        self.assertEqual(max_len, 100)

    def test_due_date(self):
        lor = LOR.objects.get(id=1)
        field_label = lor._meta.get_field('due_date').verbose_name
        self.assertEqual(field_label, 'due date')

    def test_writer_email(self):
        lor = LOR.objects.get(id=1)
        field_label = lor._meta.get_field('writer_email').verbose_name
        self.assertEqual(field_label, 'writer email')

    def test_company_name(self):
        lor = LOR.objects.get(id=1)
        field_label = lor._meta.get_field('company_name').verbose_name
        self.assertEqual(field_label, 'company name')

    def test_company_name_max_len(self):
        lor = LOR.objects.get(id=1)
        max_len = lor._meta.get_field('company_name').max_length
        self.assertEqual(max_len, 100)

    def test_company_website(self):
        lor = LOR.objects.get(id=1)
        field_label = lor._meta.get_field('company_website').verbose_name
        self.assertEqual(field_label, 'company website')

    def test_company_email(self):
        lor = LOR.objects.get(id=1)
        field_label = lor._meta.get_field('company_email').verbose_name
        self.assertEqual(field_label, 'company email')

    def test_company_recipients(self):
        lor = LOR.objects.get(id=1)
        field_label = lor._meta.get_field('company_recipients').verbose_name
        self.assertEqual(field_label, 'company recipients')

    def test_company_recipients_max_len(self):
        lor = LOR.objects.get(id=1)
        max_len = lor._meta.get_field('company_recipients').max_length
        self.assertEqual(max_len, 200)

    def test_status(self):
        lor = LOR.objects.get(id=1)
        field_label = lor._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'status')

    def test_status_max_len(self):
        lor = LOR.objects.get(id=1)
        max_len = lor._meta.get_field('status').max_length
        self.assertEqual(max_len, 20)

    def test_cv(self):
        lor = LOR.objects.get(id=1)
        field_label = lor._meta.get_field('cv').verbose_name
        self.assertEqual(field_label, 'cv')

    def test_resume(self):
        lor = LOR.objects.get(id=1)
        field_label = lor._meta.get_field('resume').verbose_name
        self.assertEqual(field_label, 'resume')

    def test_transcript(self):
        lor = LOR.objects.get(id=1)
        field_label = lor._meta.get_field('transcript').verbose_name
        self.assertEqual(field_label, 'transcript')

    def test_additional_info(self):
        lor = LOR.objects.get(id=1)
        field_label = lor._meta.get_field('additional_info').verbose_name
        self.assertEqual(field_label, 'additional info')