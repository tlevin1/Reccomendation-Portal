from django.test import TestCase
from django.urls import reverse, resolve
from requestor_manage import views


class Requestor_manage_test_url(TestCase):
    def test_submitRequest(self):
        url = reverse('request_view')
        self.assertEqual(resolve(url).func, views.request_view)