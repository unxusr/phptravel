from Src.test_base.web_driver_setup import WebDriverSetup
from Src.page_object.pages.admin_page import AdminPage, AdminManagement
from Test.Scripts.test_authentication import AuthenticationAdminUser
from Test.Scripts.generate_data import generate_data
#from Test.Scripts.test_add_admin import AddNewAdmin
import unittest 
from selenium import webdriver
import selenium.webdriver.common.keys as k
from time import sleep
import json

class EditNewAdmin(WebDriverSetup):
    
    def test_edit_new_admin_permission(self):
        driver = self.driver
        driver.get('https://phptravels.com/demo')
        driver.set_page_load_timeout(30)
        AuthenticationAdminUser.test_authentication(self)
        admin_mngmt = AdminManagement(driver)
        
        # Execute generate data function 
        with open('generated_data.json', 'r') as dt:
             user = json.load(dt)
        user = user['data'][0]

        admin_mngmt.accounts_tab().click()
        admin_mngmt.admin_accounts().click()
        admin_mngmt.edit_new_admin_button().click()
        admin_mngmt.add_location_permission().click()
        admin_mngmt.edit_location_permission().click()
        admin_mngmt.submit_new_admin_form().click()  # the same submit button as in create new admin

if __name__ == '__main__':
    unittest.main()
