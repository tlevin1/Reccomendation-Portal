from django.test import TestCase, Client
from django.urls import reverse, resolve
from datetime import datetime
from .views import writer_more_info, view_more_info
from .models import moreinfo
from  .forms import Infoform
# Create your tests here.
class TestViews(TestCase):


    def test_moreinfo_view(self):
        self.client = Client()
        self.req_url = reverse('writer_more_info')

        response = self.client.get(reverse('writer_more_info'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'more_info/moreinfo.html')

    #testing to see if there is a 200 response and using correct template

    def test_moreinfo_view2(self):
        self.client = Client()
        self.req_url = reverse('view_more_info')
        response = self.client.get(reverse('view_more_info'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'more_info/viewmoreinfo.html')

  # testing to see if there is a 200 response and using correct template
    def test_moreinfo_model_create_test(self):
        self.moreinfo = moreinfo.objects.create(
        name= 'Thuan',
        send_to = 'Josh',
        date = '2021-08-21',
        email = 'ttran009@gmail.com',
        type = 'Transcript',
        description = 'I need to see transcript to finish request'
        )
        self.moreinfo.save()
        #create new object model upload and saving it

        self.info1 =  moreinfo.objects.latest('name')
        self.info2 =  moreinfo.objects.latest('send_to')
        self.info3 =  moreinfo.objects.latest('date')
        self.info4 =  moreinfo.objects.latest('email')
        self.info5 = moreinfo.objects.latest('type')
        self.info6 =  moreinfo.objects.latest('description')
        self.assertEquals(self.info1.name, 'Thuan')
        self.assertEquals(self.info2.send_to, 'Josh')
        self.assertEquals(self.info1.email, 'ttran009@gmail.com')
        self.assertEquals(self.info2.type, 'Transcript')
        self.assertEquals(self.info3.description, 'I need to see transcript to finish request')
        #seeing if model object saved is equal

    def test_moreinfo_post(self):
        response = self.client.post(reverse('writer_more_info'), {
            'name': 'thuan',
            'send_to': 'transcript',
            'date': '2020-02-12',
            'email': 'thuan402@gmail.com',
            'type': 'CV',
            'descriptions': 'i need a copy of your CV',
        })

        self.assertEquals(response.status_code, 200)

    # testing to see if Post was succesful
class TestURL(TestCase):

        def test_moreinfo_url(self):
            url = reverse('writer_more_info')
            self.assertEqual(resolve(url).func, writer_more_info)
            # test to see if it is correct url

        def test_moreinfo_url2(self):
            url = reverse('writer_more_info')
            self.assertNotEqual(resolve(url).func, view_more_info)
            # test to see if it is correct url and not something else
        def test_viewinfo_url(self):
            url = reverse('view_more_info')
            self.assertEqual(resolve(url).func, view_more_info)
            # test to see if it is correct url

        def test_viewinfo_url2(self):
            url = reverse('view_more_info')
            self.assertNotEqual(resolve(url).func, writer_more_info)
            # test to see if it is correct url and not something else


class TestForMoreInfo(TestCase):
    def test_moreinfo_form(self):
        form = Infoform(data={
            'name': 'thuan',
            'send_to': 'transcript',
            'date': '2020-02-12',
            'email': 'thuan402@gmail.com',
            'type': 'CV',
            'description': 'i need a copy of your CV',
            })

        self.assertEqual(form.data['name'], 'thuan')
        self.assertEqual(form.data['send_to'], 'transcript')
        self.assertEqual(form.data['date'], '2020-02-12')
        self.assertEqual(form.data['email'], 'thuan402@gmail.com')
        self.assertEqual(form.data['type'], 'CV')
        self.assertEqual(form.data['description'], 'i need a copy of your CV')
    #testinf form to see if it is valid and data matches.