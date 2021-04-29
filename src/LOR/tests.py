# Create your tests here.
# put all tests here eventually

from sys import platform
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Authentication.models import LorUser as User
from Authentication.models import UserRoles as Roles

# Create your tests here.
'''
class SeleniumTests(LiveServerTestCase):
    def setUp(self):
        # create writer and requesters and one admin
        ad_user = User.objects.create_user(username='ad0',
                email='ad@umbc.edu', password='justapwd12',
                role=Roles.ADMIN)
        ad_user.save()
        rq_user = User.objects.create_user(username='rq',
                email='rq@umbc.edu', password='justapwd12',
                role=Roles.REQUESTER)
        rq_user.save()
        wr_user0 = User.objects.create_user(username='wr0',
                email='wr0@umbc.edu', password='justapwd12',
                role=Roles.WRITER)
        wr_user0.save()
        wr_user1 = User.objects.create_user(username='wr1',
                email='wr1@umbc.edu', password='justapwd12',
                role=Roles.WRITER)
        wr_user1.save()
        chromedriver_path = '../venv/Scripts/chromedriver.exe'
        base_url_path = 'http://127.0.0.1:8000/'
        if platform == 'linux' or platform == 'linux2':
            chromedriver_path = '../venv/Scripts/chromedriver_l'
        elif platform == 'darwin':
            chromedriver_path = '../venv/Scripts/chromedriver_m'
        self.browser = webdriver.Chrome(chromedriver_path)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def testform(self):
        ad_login = self.client.login(username='ad0', password='justapwd12')
        base_url_path = 'http://localhost:8000'
        submitRequest_path = '/submitRequest/'
        self.browser.get(base_url_path + submitRequest_path)
        assert self.browser.title == 'Requesting form'
'''