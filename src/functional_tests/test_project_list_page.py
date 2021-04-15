from selenium import webdriver
from budget.models import Project
from django.contrib.staticfiles.testing import StaticLiveServerTestCase



class TestProjectListPage(StaticLiveServerTestCase):

   def setUp(self):
       #test chrome browser
       self.browser = webdriver.Chrome('ReccomendationPortal/functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_no_project_alert_is_displayed(self):
       self.browser.get(self.live_server_url)
       time.sleep(20)