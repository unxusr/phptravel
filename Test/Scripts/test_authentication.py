from Src.page_object.pages.demo_page import DemoHomePage
from Src.test_base.web_driver_setup import WebDriverSetup
from Src.page_object.pages.admin_page import AdminPage
import unittest
from selenium import webdriver
from time import sleep

class AuthenticationAdminUser(WebDriverSetup):

    def test_authentication(self):
        driver = self.driver
        self.driver.get('https://phptravels.com/demo')
        self.driver.set_page_load_timeout(30)
        admin_page = AdminPage(driver)
        admin_page.admin_link().click()

        # Clicking the Admin link opens new tab so we need to switch to that tab
        self.driver.switch_to.window(driver.window_handles[1])

        admin_page.admin_email().send_keys("admin@phptravels.com")
        admin_page.admin_password().send_keys("demoadmin")
        admin_page.admin_login().click()
        self.assertEqual(admin_page.admin_dashboard().text,'DASHBOARD')


if __name__ == '__main__':
    unittest.main()
