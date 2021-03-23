from django.test import TestCase
from .models import LOR


# Create your tests here.
class LORModelTest(TestCase):
    def test_good_to_string(self):
        lor = LOR(requester_email="j@umbc.edu", writer_email="k@umbc.edu", status="pending", due_date="2021-01-01",
                  position="developer")
        self.assertEqual(str(lor), "j@umbc.edu k@umbc.edu pending 2021-01-01")
