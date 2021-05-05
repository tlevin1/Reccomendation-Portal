
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
import unittest
from Authentication.models import LorUser as User
from django.test import Client
from django.shortcuts import render, redirect
from selenium.webdriver.support import expected_conditions as EC
import time
from Authentication.models import UserRoles as Roles

class HomeViewButtonTest(TestCase):
    def setUp(self):
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
    #cookies code
    # def test_use_django_selenium_login_to_force_login(self):
    #     user = self.client.login(username = "admin", password='pass')
    #     cookie = self.client.cookies['sessionid']
    #     self.browser.get(
    #         self.live_server_url)  # selenium will set cookie domain based on current page domain
    #     self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
    #     self.browser.refresh()  # need to update page for logged in user
    #     self.browser.get(self.live_server_url)


    def test_login_using_google(self):
        #ad_login = self.client.login(username='rq', password='justapwd12')
        # This example requires Selenium WebDriver 3.13 or newer
        with webdriver.Chrome() as driver:
            wait = WebDriverWait(driver, 10)

            driver.get("http://127.0.0.1:8000/Authentication/")
            #time.sleep(15)
            #driver.find_element_by_css_selector("input[name='Home'][value='Home']").click()
            driver.find_element_by_tag_name("button").click()
            wait = WebDriverWait(driver, 5)
            username = driver.find_element_by_class_name('Xb9hP').find_element_by_name('identifier')
            username.send_keys('throwaway384745@gmail.com'+Keys.ENTER)
            time.sleep(2000)
            password = driver.find_element_by_class_name('Xb9hP').find_element_by_name('password')
            password.send_keys('hello'+Keys.ENTER)
            driver.implicitly_wait(25)
            #wait.until(EC.presence_of_element_located((By.ID, "Passwd"))).send_keys(Keys.ENTER)
            #WebDriverWait(driver,5).until(presence_of_element_located((By.NAME, "password")))
            #time.sleep(700)
            #wait = WebDriverWait(driver, 120)
            # driver.find_element_by_class_name('rFrNMe ze9ebf YKooDc q9Nsuf zKHdkd sdJrJc').find_element_by_tag_name('input').send_keys('throwawayworld12' + Keys.ENTER)

            #first_result.send_keys('throwawayworld12' + Keys.ENTER)
            #print(driver.page_source)

    def test_index_home_page(self):
        client = Client()
        response = client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)

    def test_writer_url(self):
        #login
        r_user1 = User.objects.create_user(username='r_user1', email='r1@umbc.edu', password='justapwd12')
        login = self.client.login(username='r_user1', password='justapwd12')
        response = self.client.get('http://127.0.0.1:8000/writer/')
        self.assertEqual(response.status_code, 200)


    # def test_clicked_home_button(self,request):
    #     r_user1 = User.objects.create_user(username='r_user1', email='r1@umbc.edu', password='justapwd12')
    #     login = self.client.login(username='r_user1', password='justapwd12')
    #     response = self.client.get('http://127.0.0.1:8000/writer/')
    #     self.assertEqual(response.status_code, 200)
        # if 'Home' in request.POST:
        #     print('clicked home')
