from django.test import TestCase
from django.urls import reverse, resolve
from LOR import views


class LOR_test_url(TestCase):

    def test_submitRequest(self):
        url = reverse('requesting')
        self.assertEqual(resolve(url).func, views.view_enter_request)