from Src.test_base.web_driver_setup import WebDriverSetup
from Src.page_object.pages.admin_page import AdminPage, AdminManagement
from Test.Scripts.test_authentication import AuthenticationAdminUser 
from Test.Scripts.generate_data import generate_data
import unittest 
from selenium import webdriver
import selenium.webdriver.common.keys as k
from time import sleep
import json

class AddNewAdmin(WebDriverSetup):
    
    def test_add_admin(self):
        driver = self.driver
        driver.get('https://phptravels.com/demo')
        driver.set_page_load_timeout(30)
        AuthenticationAdminUser.test_authentication(self)      
        admin_mngmt = AdminManagement(driver)
        
        # Execute generate data function 
        print(generate_data)

        with open('generated_data.json', 'r') as dt:
            user = json.load(dt)
        user = user['data'][0]

        admin_mngmt.accounts_tab().click()
        admin_mngmt.admin_accounts().click()
        admin_mngmt.add_admin_button().click()
        admin_mngmt.fill_in_first_name().send_keys(user['first_name'])
        admin_mngmt.fill_in_last_name().send_keys(user['last_name'])
        admin_mngmt.fill_in_email().send_keys(user['email'])
        admin_mngmt.fill_in_password().send_keys('demoadminuser')
        admin_mngmt.fill_in_phone().send_keys(user['phone'])
        admin_mngmt.fill_in_address_1().send_keys(user['address1'])
        admin_mngmt.fill_in_address_2().send_keys(user['address2'])
        admin_mngmt.fill_in_country().click()
        admin_mngmt.fill_in_country().send_keys(user['country'])
        admin_mngmt.fill_in_country().send_keys(k.Keys.ENTER)

if __name__ == '__main__':
    unittest.main()
