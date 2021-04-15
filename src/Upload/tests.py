from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import upload_file, upload_view, delete_upload
from .models import Upload
from  .form import Uploadform
# Create your tests here.
class TestViews(TestCase):


    def test_Upload_view(self):
        self.client = Client()
        self.req_url = reverse('upload_file')

        response = self.client.get(reverse('upload_file'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Upload/upload.html')

    #testing to see if there is a 200 response and using correct template

    def test_Upload_view2(self):
        self.client = Client()
        self.req_url = reverse('upload_view')
        response = self.client.get(reverse('upload_view'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Upload/uploadview.html')

    # testing to see if there is a 200 response and using correct template
    def test_upload_post(self):
        self.upload = Upload.objects.create(
        name= 'thuan',
        type = 'pdf',
        pdf = 'Upload/pdf/ER_DIAGRAM.pdf',
        )
        self.upload.save()
        #create new object model upload and saving it

        self.upload2 = Upload.objects.latest('name')
        self.upload3 = Upload.objects.latest('type')
        self.upload4 = Upload.objects.latest('pdf')
        self.assertEquals(self.upload2.name, 'thuan')
        self.assertEquals(self.upload3.type, 'pdf')
        self.assertEquals(self.upload4.pdf, 'Upload/pdf/ER_DIAGRAM.pdf')
        #pulling lastest object model and testing to see if its the same

        response = self.client.post(reverse('upload_file'), {
            'name' : 'thuan',
            'type' : 'transcript',
            'pdf' : 'Upload/pdf/ER_DIAGRAM.pdf',

        })
        #post request with a new object
        self.assertEquals(response.status_code, 200)
        #testing to see if Post was succesful
        self.assertEquals(self.upload.name, 'thuan')
        self.assertEquals(self.upload.type, 'pdf')
        self.assertEquals(self.upload.pdf, 'Upload/pdf/ER_DIAGRAM.pdf')
        #testing to see if variable are still correct

    def test_delete_upload_post(self):
        self.upload = Upload.objects.create(
        name= 'Jacob',
        type = 'pdf',
        pdf = 'Upload/pdf/ER_DIAGRAM.pdf',
        )
        self.upload.save()
        response = self.client.post(reverse('delete_upload', args=[1]))
        self.assertEquals(response.status_code, 200)
        # testing to see if Post was succesful

class TestURL(TestCase):

        def test_upload_url(self):
            url = reverse('upload_file')
            self.assertEqual(resolve(url).func, upload_file)
            # test to see if it is correct url

        def test_upload_view_url(self):
            url = reverse('upload_view')
            self.assertEqual(resolve(url).func, upload_view)
            # test to see if it is correct url

        def test_delete_upload_view_url(self):
            url = reverse('delete_upload', args=[1])
            self.assertEqual(resolve(url).func, delete_upload)
            # test to see if it is correct url


class Testmodels(TestCase):

            def test_model_upload(self):
                self.upload = Upload.objects.create(
                    name='Joshua',
                    type='transcript',
                    pdf='Upload/pdf/ER_DIAGRAM.pdf',
                )
                self.assertEquals(self.upload.name, 'Joshua')
                self.assertEquals(self.upload.type, 'transcript')
                self.assertEquals(self.upload.pdf, 'Upload/pdf/ER_DIAGRAM.pdf')
                # test to see if all objects variable are correct

