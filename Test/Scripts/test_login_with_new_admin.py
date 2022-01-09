from Src.test_base.web_driver_setup import WebDriverSetup
from Src.page_object.pages.admin_page import AdminPage
import unittest
from selenium import webdriver
from time import sleep
import json

class AuthenticationNewAdminUser(WebDriverSetup):

    def test_new_admin_authentication(self):
        driver = self.driver
        driver.get('https://phptravels.com/demo')
        driver.set_page_load_timeout(30)
        admin_page = AdminPage(driver)
        admin_page.admin_link().click()

        with open('generated_data.json', 'r') as dt:
            user = json.load(dt)
        user = user['data'][0]

        # Clicking the Admin link opens new tab so we need to switch to that tab
        driver.switch_to.window(driver.window_handles[1])

        admin_page.admin_email().send_keys(user['email'])
        admin_page.admin_password().send_keys("demoadminuser")
        admin_page.admin_login().click()
        self.assertEqual(admin_page.admin_dashboard().text,'DASHBOARD')


if __name__ == '__main__':
    unittest.main()
