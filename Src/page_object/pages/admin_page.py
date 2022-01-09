import sys
import os
from selenium.webdriver.common.by import By
from Src.page_object.locators import Locator

class AdminPage(object):
    def __init__(self, driver):
        self.driver = driver

    def admin_link(self):
        return self.driver.find_element(By.XPATH, Locator.admin_backend_link)
        
    def admin_email(self):
        return self.driver.find_element(By.XPATH, Locator.login_email)
    
    def admin_password(self):
        return self.driver.find_element(By.XPATH, Locator.login_password)
    
    def admin_login(self):
        return self.driver.find_element(By.XPATH, Locator.login_button)
    
    def admin_dashboard(self):
        return self.driver.find_element(By.XPATH, Locator.dashboard_title)


class AdminManagement(object):
    def __init__(self, driver):
        self.driver = driver

    def accounts_tab(self):
        return self.driver.find_element(By.XPATH, Locator.accounts_tab)

    def admin_accounts(self):
        return self.driver.find_element(By.XPATH, Locator.admin_page_link)

    def add_admin_button(self):
        return self.driver.find_element(By.XPATH, Locator.add_new_admin_button)

    def fill_in_first_name(self):
        return self.driver.find_element(By.XPATH, Locator.first_name)
    
    def fill_in_last_name(self):
        return self.driver.find_element(By.XPATH, Locator.last_name)

    def fill_in_email(self):
        return self.driver.find_element(By.XPATH, Locator.email)

    def fill_in_password(self):
        return self.driver.find_element(By.XPATH, Locator.password)
    
    def fill_in_phone(self):
        return self.driver.find_element(By.XPATH, Locator.phone)

    def fill_in_country(self):
        return self.driver.find_element(By.XPATH, Locator.country)

    def fill_in_address_1(self):
        return self.driver.find_element(By.XPATH, Locator.address1)
    
    def fill_in_address_2(self):
        return self.driver.find_element(By.XPATH, Locator.address2)
    
    def submit_new_admin_form(self):
        return self.driver.find_element(By.XPATH, Locator.submit)

    def edit_new_admin_button(self):
        return self.driver.find_element(By.XPATH, Locator.admin_edit_button)

    def add_location_permission(self):
        return self.driver.find_element(By.XPATH, Locator.add_location_checkbox)

    def edit_location_permission(self):
        return self.driver.find_element(By.XPATH, Locator.edit_location_checkbox)

    def confirm_admin_email(self):
        return self.driver.find_element(By.XPATH, Locator.admin_email)