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
    